"""
Retreive topo and dtopo files that are stored on the s3 server that are
required for the Crescent City Simulations
"""
import boto
from boto.s3.key import Key
from boto.s3.connection import Location
import os, sys
import keys
import csv
from numpy import genfromtxt
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
import user_info_file

user = user_info_file.user_info()
driver = driver_import.driver_info(1)

###########################
## Find Specified Bucket ##
###########################

def find_s3_bucket(s3_conn, string):
    print 'Finding Bucket'
    for i in s3_conn.get_all_buckets():
        if string in i.name:
            return i

###############################
## Download A Specified File ##
###############################

def download_file(file_name, bucket_name):
    print 'Downloading %s from s3 storage bucket %r'%(file_name,bucket_name)
    k.key = file_name
    k.get_file(open(file_name,'w'))
    return
##################
## Main Program ##
##################
        
print "Downloading files from S3"
AWS_ACCESS_KEY_ID = keys.aws_key('access')
AWS_SECRET_ACCESS_KEY = keys.aws_key('secret')

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bucket_name = user.topo_bucket
bucket = find_s3_bucket(conn, bucket_name)
k = Key(bucket)

#accesses the full list of files in the bucket
file_list = bucket.get_all_keys()

# Make etopo dir
#CCdir = '/home/jonathan/research/aws_automation'
CCdir = '/home/ubuntu/CC'
subdir = 'topo'
os.system('mkdir -p %s'%subdir)
os.chdir(subdir)

print "Downloading topo files to %r from AWS S3:"%subdir

topo_list = '/home/ubuntu/topo_list.csv'
topo_block =  genfromtxt(topo_list, dtype=None, delimiter=',')

for row in topo_block:
    fname = row[0]
    download_file(fname,bucket_name)


#Download driver.source from s3 to local dtopo directory
subdir ='dtopo'
os.chdir(CCdir)
os.system('mkdir -p %s'%subdir)
os.chdir(subdir)

print "Downloading dtopo files to %r"%subdir
fname = driver.source
download_file(fname,bucket_name)

