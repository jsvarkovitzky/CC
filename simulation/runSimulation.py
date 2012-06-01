"""                                                                             
Start simulation and 
"""                                                                             
                                                                                
from setrun import setrun                                                       
from setplot import setplot                                                     
from pyclaw.runclaw import runclaw                                              
from pyclaw.plotters.plotclaw import plotclaw                                   
import os
import datetime
from upload_results import upload_results_s3


now = datetime.datetime.now()
# initialize rundata using setrun but then change some things for each run:     
rundata = setrun()

os.system('make clean')
os.system('make .plots')
upload_results_s3(now)
os.system('halt')
