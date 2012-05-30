"""                                                                             
Start simulation and 
"""                                                                             
                                                                                
from setrun import setrun                                                       
from setplot import setplot                                                     
from pyclaw.runclaw import runclaw                                              
from pyclaw.plotters.plotclaw import plotclaw                                   
                                                                                
# initialize rundata using setrun but then change some things for each run:     
rundata = setrun()

runclaw(xclawcmd = "xgeoclaw", outdir="_output_1level")
plotclaw(outdir="_output_1level", plotdir="_plots_1level")

