# This program tests the functionality of reading in csv files
# Jonathan Varkovitzky
# May 16, 2012

import csv
from numpy import *

class driver_info:
    def __init__(self,runid):
        driver_file = '/home/ubuntu/Driver.csv'
        driver_block = genfromtxt(driver_file, dtype=None, delimiter=',', names=True)
        driver_list = driver_block[runid-1]
    
        self.runid = driver_list[0]
        self.source = driver_list[1]
        self.mxnest = driver_list[2]
        self.inratx = [driver_list[3],driver_list[4],driver_list[5],driver_list[6],driver_list[7]]
        self.topofile = driver_list[7]
        self.subdomain = driver_list[8]
        self.fg_file = driver_list[9]





