#Uploads final ouputs and plots to s3
#Jonathan Varkovitzky
#May 29, 2012

import boto
import sys
import os
from boto.s3.key import Key
from boto.s3.connection import Location
#import /home/ubuntu/CC/simulation/keys

############################
## tar provided directory ##
############################

def tar_dir(dir_name):
    tar_name = str(dir_name + '.tar')
    os.system('tar -czf' + repr(tar_name) + ' ' + repr(dir_name))

dirName = '_output'
tar_dir(dirName)
