# Read in the provided plot_list.csv file and assign the relavant values to objects 
# That can be called later on by setplot.py
# Jonathan Varkovitzky
# June 7, 2012

import csv
from numpy import *

class plot_info:
    def __init__(self,plot_id):
        plot_file = '/home/ubuntu/plot_list.csv'
        plot_block = genfromtxt(plot_file, dtype=None, delimiter=',', names=True)
        plot_list = plot_block[plot_id-1]
    
        self.name = plot_list[0]
	self.title = plot_list[1]
	self.xlower = plot_list[2]
	self.xupper = plot_list[3]
	self.ylower = plot_list[4]
	self.yupper = plot_list[5]
	self.cmin = plot_list[6]
	self.cmax = plot_list[7]



