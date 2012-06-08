
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 


from pyclaw.geotools import topotools
from pyclaw.data import Data
import pylab
import glob
from numpy import loadtxt

try:
    TG_19750 = loadtxt('../19750_notide.txt')
except:
    print "*** could not load tide gauge data"

try:
    from setplotfg import setplotfg
except:
    print "Did not find setplotfg.py"
    setplotfg = None

lib_path = os.path.abspath('../../')
sys.path.append(lib_path)
import plot_import



# --------------------------
def setplot(plotdata):
# --------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    from pyclaw.plotters import colormaps, geoplot

    plotdata.clearfigures()  # clear any old figures,axes,items dat
#   plotdata.format = "netcdf"

    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:

    def addgauges(current_data):
        from pyclaw.plotters import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
             gaugenos='all', format_string='ko', add_labels=True)

    def title_hours(current_data):
        from pylab import title
        t = current_data.t
        h = t/3600.
        title('%5.2f Hours after Quake' % h)

    def plotcc(current_data):
        from pylab import plot,text
        plot([235.8162], [41.745616],'wo')
        text(235.8,41.9,'Cr.City',color='w',fontsize=10)
    

    # Calculate length of plot_list
    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    for i in range(0,file_len(plot_list.csv)-1):
        plot_settings = plot_import.plot_info(i+1)
        
        #-----------------------------------------
        # Set Figure Parameters
        #-----------------------------------------
        plotfigure = plotdata.new_plotfigure(name=plot_settings.name, figno=i)
        plotfigure.kwargs = {'figsize': (16,4)}
        plotfigure.show = True

    # Set up for axes in this figure:
        plotaxes = plotfigure.new_plotaxes()
        plotaxes.title = plot_settings.title
        plotaxes.scaled = True
        
        def aa(current_data):
            title_hours(current_data)
            if 0:
                from pylab import savefig
                fname = 'pacific%s.png' % str(current_data.frameno).zfill(4)
            savefig(fname)
            print 'Saved ',fname
        plotaxes.afteraxes = aa

        # Water
        plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
        plotitem.plot_var = geoplot.surface_or_depth
        my_cmap = colormaps.make_colormap({-1.0: [0.0,0.0,1.0], \
                                     -0.1: [0.5,0.5,1.0], \
                                      0.0: [1.0,1.0,1.0], \
                                      0.1: [1.0,0.5,0.5], \
                                      1.0: [1.0,0.0,0.0]})
        plotitem.imshow_cmap = my_cmap
        plotitem.imshow_cmin = plot_settings.cmin
        plotitem.imshow_cmax = plot_settings.cmax
        plotitem.add_colorbar = True
        plotitem.amr_gridlines_show = [0,0,0]
        plotitem.amr_gridedges_show = [1]

        # Land
        plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
        plotitem.plot_var = geoplot.land
        plotitem.imshow_cmap = geoplot.land_colors
        plotitem.imshow_cmin = 0.0
        plotitem.imshow_cmax = 100.0
        plotitem.add_colorbar = False
        plotitem.amr_gridlines_show = [0,0,0]
        plotitem.amr_gridedges_show = [0]
        plotaxes.xlimits = [plot_settings.xlower,plot_settings.xupper] 
        plotaxes.ylimits = [plot_settings.ylower,plot_settings.yupper]
        #plotaxes.afteraxes = addgauges
        
        # Add contour lines of bathymetry:
        plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
        #plotitem.show = False
        plotitem.plot_var = geoplot.topo
        from numpy import arange, linspace
        plotitem.contour_levels = linspace(-6000,0,7)
        plotitem.amr_contour_colors = ['g']  # color on each level
        plotitem.kwargs = {'linestyles':'solid'}
        plotitem.amr_contour_show = [0,0,1,0]  # show contours only on finest level
        plotitem.gridlines_show = 0
        plotitem.gridedges_show = 0
        
        # Add contour lines of topography:
        plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
        plotitem.show = False
        plotitem.plot_var = geoplot.topo
        from numpy import arange, linspace
        plotitem.contour_levels = arange(0., 11., 1.)
        plotitem.amr_contour_colors = ['g']  # color on each level
        plotitem.kwargs = {'linestyles':'solid'}
        plotitem.amr_contour_show = [0,0,0,1]  # show contours only on finest level
        plotitem.gridlines_show = 0
        plotitem.gridedges_show = 0

    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='gauge plot', figno=300, \
                    type='each_gauge')
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [9*3600, 19*3600]
    #plotaxes.xlimits = [8*3600, 15*3600]
    plotaxes.ylimits = [-0.5,0.5]
    plotaxes.title = 'Surface'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 3
    plotitem.plotstyle = 'b-'

    # Plot topo as green curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.show = False
    def gaugetopo(current_data):
        q = current_data.q
        h = q[:,0]
        eta = q[:,3]
        topo = eta - h
        return topo
    plotitem.plot_var = gaugetopo
    plotitem.plotstyle = 'g-'


    def fix_gauge(current_data):
        from pylab import plot, legend, xticks, floor, yticks
        t = current_data.t
        gaugeno = current_data.gaugeno
        if gaugeno == 19750:
            plot(TG_19750[:,0],TG_19750[:,1],'r')
            legend(('GeoClaw','Tide Gauge'),loc='lower left')
        #plot([0,10800],[0,0],'k')
        n = int(floor(t.max()/3600.) + 2)
        xticks([3600*i for i in range(n)],[str(i) for i in range(n)],\
          fontsize=15)
        yticks(fontsize=15)

    plotaxes.afteraxes = fix_gauge


    #-----------------------------------------
    # Figure for contour plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='contour', figno=1)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0,1]
    plotaxes.ylimits = [0,1]
    plotaxes.title = 'Solution'
    plotaxes.scaled = True

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.surface
    plotitem.contour_nlevels = 40
    plotitem.contour_min = -0.1
    plotitem.contour_max = 0.1
    plotitem.amr_contour_colors = ['r','k','b']  # color on each level
    plotitem.amr_contour_show = [0,1]            # show lines on each level?
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.amr_grid_bgcolor = ['#ffeeee', '#eeeeff', '#eeffee']
    plotitem.show = True 

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.land
    plotitem.contour_nlevels = 40
    plotitem.contour_min = 0.0
    plotitem.contour_max = 100.0
    plotitem.amr_contour_colors = ['g']  # color on each level
    plotitem.amr_grid_bgcolor = ['#ffeeee', '#eeeeff', '#eeffee']
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = False 

    # Fixed grid plots:
    # -----------------

    if setplotfg is not None:

        # Repeat as desired for other fixed grids...
	# These show up when using 'make .plots'
        otherfig = plotdata.new_otherfigure('Fixed Grid 1')
        fgno = 1
        sfgno = str(fgno).zfill(2)  # e.g. '01'
        otherfig.fname = '_PlotIndex_FixedGrid%s.html' % sfgno
        def make_fgplots(plotdata):
            fgdata = setplotfg(fgno, outdir=plotdata.outdir)
            # See the setplotfg function for setting up fixed grid plots
            fgdata.fg2html(framenos='all')
        otherfig.makefig = make_fgplots


    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

    
