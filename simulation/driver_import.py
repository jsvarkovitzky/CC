# This program tests the functionality of reading in csv files
# Jonathan Varkovitzky
# May 16, 2012

import csv
from numpy import *

class driver_info:
    def __init__(self,runid):
        driver_file = '/home/ubuntu/Driver_Test.csv'
        driver_block = genfromtxt(driver_file, dtype=None, delimiter=',', names=True)
        driver_list = driver_block[runid-1]
    
        self.runid = driver_list[0]
        self.source = driver_list[1]
        self.refine = driver_list[2]





