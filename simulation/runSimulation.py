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

#Take timestamp at the moment this script is called
now = datetime.datetime.now()
# initialize rundata using setrun but then change some things for each run:     
rundata = setrun()

#Make sure that any erronious files are removed and beginssimulation
os.system('make clean')
os.system('make .plots')

#Compress and upload files using the timestamp created earlier
upload_results_s3(now)

#Automatically shut down the instance
os.system('sudo halt')
