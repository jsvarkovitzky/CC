"""                                                                             
Start simulation and 
"""                                                                             
                                                                                
from setrun import setrun                                                       
from setplot import setplot                                                     
from pyclaw.runclaw import runclaw                                              
from pyclaw.plotters.plotclaw import plotclaw                                   
                                                                                
# initialize rundata using setrun but then change some things for each run:     
rundata = setrun()

runclaw(xclawcmd = "xgeoclaw", outdir="_output")
plotclaw(outdir="_output", plotdir="_plots")

upload_results()
