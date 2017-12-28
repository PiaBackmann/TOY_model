# WriteTemplate.py
# This script is used for the automatic generation of
# Netlogo-files for running them automatically with
# varying values for tab-data
# input: 
#   - nlogo-file with template-strings
#   - parameters in this file
# output:
#   - nlogo-file with values

def seq(start, stop, step=1):
    n = int(round((stop - start)/float(step)))
    if n > 1:
        return([round(start + step*i,2) for i in range(n+1)])
    else:
        return([])

import string
import os
import shutil
import tempfile
from subprocess import call
from time import strftime as date
import glob
import sys
import string

cwd = (os.getcwd())
runtimestamp = date('%Y-%m-%d-%H-%M-%S')

# choose filepath for results - either:
#   - each model-run in a different folder (named with timestamp)
#   - all in the same folder ('out') - maybe more convenient
filepath = cwd + "\\" + str(runtimestamp)
filepath = cwd + "\\" + str('out')
os.makedirs(filepath)

inputfile = open('template.nlogo','r').read()

filenumber = 1
runnumber = 1

#==========================================
# Parameters
#==========================================

disturbance_chance = [0]
disturbance_range = [2.0]
disturbance_severity = [30]
mortality_rate = [0.01]
worldsize = [256]
runs = [1]                 # How many times is each parameter combination run seperately?
endtime = [10001]       # How many timestep (== years) should the model run?
clusterout = "1 500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000 6500 7000 7500 8000 8500 9000 9500 10001"

dispersalrange1 = [1]
dispersalrange2 = [20]	
dispersalrange3 = [20]	
dispersalrange4 = [20]	
dispersalrange5 = [20]  
dispersalrange6 = [20]  
dispersalrange7 = [20]  
dispersalrange8 = [20]

seednumber1 = [9415]	
seednumber2 = [20]
seednumber3 = [20]
seednumber4 = [20]
seednumber5 = [20]
seednumber6 = [20]
seednumber7 = [20]
seednumber8 = [20]

shadetolerance1 = [50]
shadetolerance2 = [50]
shadetolerance3 = [50]
shadetolerance4 = [50]
shadetolerance5 = [50]
shadetolerance6 = [50]
shadetolerance7 = [50]
shadetolerance8 = [50]

similaradjustment1 = [0]
similaradjustment2 = [0]
similaradjustment3 = [0]
similaradjustment4 = [0]
similaradjustment5 = [0]
similaradjustment6 = [0]
similaradjustment7 = [0]
similaradjustment8 = [0]

sameadjustment1 = [0]
sameadjustment2 = [0]
sameadjustment3 = [0]
sameadjustment4 = [0]
sameadjustment5 = [0]
sameadjustment6 = [0]
sameadjustment7 = [0]
sameadjustment8 = [0]

#==========================================
# Main Routine
#==========================================

globalparameterlist = [[a] + [b] + [c] + [d] + [e] + [f] + [g] for a in disturbance_chance for b in
        disturbance_range for c in disturbance_severity for d in mortality_rate for e in
        worldsize for f in runs for g in endtime]

dispersalrangelist = [[a]+ [b] + [c] + [d] + [e] + [f] + [g] + [h] for a in dispersalrange1 for b in dispersalrange2 for c in dispersalrange3 for d in dispersalrange4 for e in dispersalrange5 for f in dispersalrange6 for g in dispersalrange7 for h in dispersalrange8]

seednumberlist = [[a]+ [b] + [c] + [d] + [e] + [f] + [g] + [h] for a in seednumber1 for b in seednumber2 for c in seednumber3 for d in seednumber4 for e in seednumber5 for f in seednumber6 for g in seednumber7 for h in seednumber8]

shadetolerancelist = [[a]+ [b] + [c] + [d] + [e] + [f] + [g] + [h] for a in shadetolerance1 for b in shadetolerance2 for c in shadetolerance3 for d in shadetolerance4 for e in shadetolerance5 for f in shadetolerance6 for g in shadetolerance7 for h in shadetolerance8]

similaradjustmentlist = [[a]+ [b] + [c] + [d] + [e] + [f] + [g] + [h] for a in similaradjustment1 for b in similaradjustment2 for c in similaradjustment3 for d in similaradjustment4 for e in similaradjustment5 for f in similaradjustment6 for g in similaradjustment7 for h in similaradjustment8]

sameadjustmentlist = [[a]+ [b] + [c] + [d] + [e] + [f] + [g] + [h] for a in sameadjustment1 for b in sameadjustment2 for c in sameadjustment3 for d in sameadjustment4 for e in sameadjustment5 for f in sameadjustment6 for g in sameadjustment7 for h in sameadjustment8]


for dispersalrangecombination in dispersalrangelist:
    for seednumbercombination in seednumberlist:
        for shadetolerancecombination in shadetolerancelist:
            for similaradjustmentcombination in similaradjustmentlist:
                for sameadjustmentcombination in sameadjustmentlist:
                    for globalparametercombination in globalparameterlist:

                        # Assign current values to the parameters
                        disp1 = dispersalrangecombination[0];disp2 = dispersalrangecombination[1];
			disp3 = dispersalrangecombination[2];disp4 = dispersalrangecombination[3];
                        disp5 = dispersalrangecombination[4];disp6 = dispersalrangecombination[5];
			disp7 = dispersalrangecombination[6];disp8 = dispersalrangecombination[7];

                        seed1 = seednumbercombination[0]; seed2 = seednumbercombination[1]; seed3 = seednumbercombination[2]; 
			seed4 = seednumbercombination[3]; seed5 = seednumbercombination[4]; seed6 = seednumbercombination[5]; 
			seed7 = seednumbercombination[6]; seed8 = seednumbercombination[7];

                        shade1 = shadetolerancecombination[0]; shade2 = shadetolerancecombination[1]; shade3 = shadetolerancecombination[2];
			shade4 = shadetolerancecombination[3]; shade5 = shadetolerancecombination[4]; shade6 = shadetolerancecombination[5];
			shade7 = shadetolerancecombination[6]; shade8 = shadetolerancecombination[7];

                        simi1 = similaradjustmentcombination[0]; simi2 = similaradjustmentcombination[1]; 
			simi3 = similaradjustmentcombination[2]; simi4 = similaradjustmentcombination[3];
                        simi5 = similaradjustmentcombination[4]; simi6 = similaradjustmentcombination[5]; 
			simi7 = similaradjustmentcombination[6]; simi8 = similaradjustmentcombination[7];
			
			same1 = sameadjustmentcombination[0]; same2 = sameadjustmentcombination[1]; same3 = sameadjustmentcombination[2];
    			same4 = sameadjustmentcombination[3]; same5 = sameadjustmentcombination[4]; same6 = sameadjustmentcombination[5];
			same7 = sameadjustmentcombination[6]; same8 = sameadjustmentcombination[7];
			
			# Global parameters (mortality, disturbance)
			dischance = globalparametercombination[0]; disrange = globalparametercombination[1];
			dissever =  globalparametercombination[2]; mortrate = globalparametercombination[3];
			worldsize = globalparametercombination[4]; runs = globalparametercombination[5];
			endtime = globalparametercombination[6];

			# Check if seednumbers always decrease with dispersal range
			if (disp1 <= disp2) and (disp2 <= disp3) and (disp3 <= disp4) and (disp4 <= disp5) and (disp5 <= disp6) and (disp6 <= disp7) and (disp7 <= disp8):

			 # Writing of the nlogo-file where %somethings are replaced by the parameters
			 outputfile = open('output.nlogo','w')
			 output =   inputfile % (worldsize, dischance, disrange, dissever, mortrate, clusterout, \
				    disp1, disp2, disp3, disp4, disp5, disp6, disp7, disp8, \
				    seed1, seed2, seed3, seed4, seed5, seed6, seed7, seed8, \
				    shade1, shade2, shade3, shade4, shade5, shade6, shade7, shade8, \
				    simi1, simi2, simi3, simi4, simi5, simi6, simi7, simi8, \
				    same1, same2, same3, same4, same5, same6, same7, same8, \
				    worldsize, runs, endtime)
			 outputfile.write(output)
			 outputfile.close()

			 # This file contains the output from Netlogo run
			 reportfilename = filepath + '/' + 'out_' + str(filenumber) + '.tab'

			 # This file contains the parameters for the run
			 parameterfilename = filepath + '\\' + 'out_' + str(filenumber) + '.par'
			 parameterfile = open(parameterfilename,'w')
			 parameterfile.write(( str(worldsize) + ' ' + str(dischance) + ' ' + str(disrange) + ' ' + str(dissever) + ' ' + str(mortrate) + ' ' + \
				       str(disp1) + ' ' + str(disp2) + ' ' + str(disp3) + ' ' + str(disp4) + ' ' + str(disp5) + ' ' + str(disp6) + ' ' + str(disp7) + ' ' + str(disp8) + ' ' \
				     + str(seed1) + ' ' + str(seed2) + ' ' + str(seed3) + ' ' + str(seed4) + ' ' + str(seed5) + ' ' + str(seed6) + ' ' + str(seed7) + ' ' + str(seed8) + ' '  \
				     + str(shade1) + ' ' + str(shade2) + ' ' + str(shade3) + ' ' + str(shade4) + ' ' + str(shade5) + ' ' + str(shade6) + ' ' + str(shade7) + ' ' + str(shade8) + ' ' \
				     + str(simi1) + ' ' + str(simi2) + ' ' + str(simi3) + ' ' + str(simi4) + ' ' + str(simi5) + ' ' + str(simi6) + ' ' + str(simi7) + ' ' + str(simi8) + ' '  \
				     + str(same1) + ' ' + str(same2) + ' ' + str(same3) + ' ' + str(same4) + ' ' + str(same5) + ' ' + str(same6) + ' ' + str(same7) + ' ' + str(same8) + '\n')) 


			 # ==========================================
			 # Call netlogo

		    	 commandname = str("./java/bin/java -Xmx1024m -Dfile.encoding=UTF-8 -cp NetLogo.jar org.nlogo.headless.Main \
				--model output.nlogo \
				--experiment ex2 \
				--table " + reportfilename)
			 call(commandname)

			 # ==========================================
			 # World-file (contains turtles for clustering-analysis
			 for filename in glob.glob('world*.out'):
			    namelist = filename.split("_")
			    runnumber = namelist[1]
			    plottime = namelist[2]
			    worldfilename = filepath + '/' + 'turtles_' + (3-len(str(filenumber)))*"0" + str(filenumber) + '_' + (3-len(str(runnumber)))*"0" + str(runnumber) + '_' + (5-len(str(plottime)))*"0" + str(plottime) + '.out'
			    ein = open(filename)
			    aus = open(worldfilename,"w")

			    schreiben = False
    
			    for line in ein:
			        rausline = line.replace('"','')

			        if rausline.find("TURTLES") > -1:
				    schreiben = True
				
				if rausline.find("PATCHES") > -1:
				    schreiben = False
	    
				if schreiben == True:
				    aus.write(rausline)

			    aus.close(); ein.close()
			    os.remove(filename)
	    
			    # ==========================================
			    # Imagefile of world
			 for filename in glob.glob('view*.png'):
			    namelist = filename.split("_")
			    runnumber = namelist[1]
			    plottime = namelist[2]
			    viewfilename = filepath + '/' + 'view_' + (3-len(str(filenumber)))*"0" + str(filenumber) + '_' + (3-len(str(runnumber)))*"0" + str(runnumber) + '_' + (5-len(str(plottime)))*"0" + str(plottime) + '.png'
			    shutil.move(filename,viewfilename)

			 filenumber += 1
