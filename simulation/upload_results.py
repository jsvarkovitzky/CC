#Uploads final ouputs and plots to s3
#Jonathan Varkovitzky
#May 29, 2012

import boto
import sys
import os
from boto.s3.key import Key
from boto.s3.connection import Location

lib_path = os.path.abspath('../../')
sys.path.append(lib_path)

import user_info_file
import keys
user = user_info_file.user_info()

############################
## tar provided directory ##
############################

def tar_dir(dir_name,now):
    print 'Compressing the %s directory.' %dir_name
    timeStamp = time_stamp_format(now)
    print "The timestamp is %s" %timeStamp
    tar_name = str(dir_name + '_' + timeStamp + '.tar')
    #tar_name = str(dir_name + '.tar')
    os.system('tar -czf' + repr(tar_name) + ' ' + repr(dir_name))
    return tar_name
###########################
## Upload tar file to s3 ##
###########################

def upload_file(file_name, bucket_name,k):
    print 'Uploading %s to s3 storage bucket %r'%(file_name,bucket_name)
    k.key = file_name
    k.set_contents_from_filename(file_name,cb=percent_cb, num_cb=10)
    
###########################
## Find Specified Bucket ##
###########################

def find_s3_bucket(s3_conn, string):
    print 'Finding bucket on S3'
    for i in s3_conn.get_all_buckets():
        if string in i.name:
            return i

############################
## Progress Visualization ##
############################

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

###########################
## Format Timestamp Text ##
###########################

def time_stamp_format(now):
    timeStamp = str(now.year) + str('%02d'%now.month) + str('%02d'%now.day) + '_' + str('%02d'%now.hour) + str('%02d'%now.minute) + str('%02d'%now.second)    
    return timeStamp

##################
## Main Program ##
##################
def upload_results_s3(now):
    AWS_ACCESS_KEY_ID = keys.aws_key('access')
    AWS_SECRET_ACCESS_KEY = keys.aws_key('secret')
        
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
        
    dirName = ['_output','_plots']
    bucketName = [user.output_bucket,user.product_bucket]
    for i in range(0,len(dirName)):
        bucket = find_s3_bucket(conn, bucketName[i])
        k = Key(bucket)
        tar_name = tar_dir(dirName[i],now)
        upload_file(tar_name,bucket,k)
