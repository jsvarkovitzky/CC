"""
Retreive topo and dtopo files that are stored on the s3 server that are
required for the Crescent City Simulations
"""

import boto
from boto.s3.key import Key
from boto.s3.connection import Location
import os, sys
import keys

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
bucket_name = 'cc_topos'
bucket = find_s3_bucket(conn, bucket_name)
k = Key(bucket)

#accesses the full list of files in the bucket
file_list = bucket.get_all_keys()

# Make etopo dir
#CCdir = '/home/jonathan/research/aws_automation'
CCdir = '/claw/clawpack-4.x/CC'
subdir = 'topo/etopo'
os.system('mkdir -p %s'%subdir)
os.chdir(subdir)

# Download etopo files into their directory
fname = 'etopo1min139E147E34N41N.asc'
download_file(fname,bucket_name)

fname = 'etopo4min120E72W40S60N.asc'
download_file(fname,bucket_name)

# Download topo files into their directory
subdir = 'topo/CC'
os.chdir(CCdir)
os.system('mkdir -p %s'%subdir)
os.chdir(subdir)

fname = 'ca_north36secm.asc'
download_file(fname,bucket_name)

fname = 'cc-1sec-c.asc'
download_file(fname,bucket_name)

fname = 'cc-1_3sec-c.asc'
download_file(fname,bucket_name)

# Download dtopo files into their directory
subdir ='dtopo/tohuku'
os.chdir(CCdir)
os.system('mkdir -p %s'%subdir)
os.chdir(subdir)

fname = 'ucsb3-1min.tt1'
download_file(fname,bucket_name)

fname = 'fujii.txydz'
download_file(fname,bucket_name)

##
#topo_files = ([
#        'etopo1min139E147E34N41N.asc',
#        'etopo4min120E72W40S60N.asc',
#        'ca_north36secm.asc',
#        'cc-1sec-c.asc',
#        'cc-1_3sec-c.asc'])#
#
#dtopo_files([
#        'ucsb3-1min.tt1',
#        'fujii.txydz'])
