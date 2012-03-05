"""
Retreive topo and dtopo files that are stored on the s3 server that are
required for the Crescent City Simulations
"""

import boto
from boto.s3.key import Key
from boto.s3.connection import Location
import keys

###########################
## Find Specified Bucket ##
###########################

def find_s3_bucket(s3_conn, string):
    print 'Finding Bucket'
    for i in s3_conn.get_all_buckets():
        if string in i.name:
            return i
###########################
        
print "Downloading files from S3"
AWS_ACCESS_KEY_ID = keys.aws_key('access')
AWS_SECRET_ACCESS_KEY = keys.aws_key('secret')

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bucket_name = 'cc_topos'
bucket = find_s3_bucket(conn, bucket_name)

file_list = bucket.get_all_keys()
