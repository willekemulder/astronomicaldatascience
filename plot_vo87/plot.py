#!/usr/bin/python
from __future__ import unicode_literals
from __future__ import division

import astropy
from astropy.io import fits, ascii

from astroquery.sdss import SDSS
from astropy import coordinates as coords
from astropy.table import Table, Column

import numpy as np
import matplotlib
#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
from matplotlib import pyplot as plt

import os,sys
# Store current working directory
pwd = os.path.dirname(__file__)
# Append current directory to the python path
sys.path.append(pwd)


def vo_line_n(x):
	''' VO87 Diagram from http://iopscience.iop.org/article/10.1086/318944/pdf Empi(5, 6, 7) '''
	# vo_line_n describes the empirical relation between log([N II]/Ha) and log([O III]/Hb)
	y = (0.61/(x - 0.47))+1.19
	return y

def vo_line_s(x):
	''' VO87 Diagram from http://iopscience.iop.org/article/10.1086/318944/pdf Empi(5, 6, 7) '''
	# vo_line_s describes the empirical relation between log([S II]/Ha) and log([O III]/Hb)
	y = (0.72/(x - 0.32))+1.30
	return y

def vo_line_o(x):
	''' VO87 Diagram from http://iopscience.iop.org/article/10.1086/318944/pdf Empi(5, 6, 7) '''
	# vo_line_o describes the empirical relation between log([O I]/Ha) and log([O III]/Hb)
	y = (0.73/(x + 0.59))+1.33
	return y

def ratio(data, x_raw1, x_raw2, y_raw1, y_raw2):
	''' Calculation of the values of the log(emission line ratios) to be plotted on the VO87 diagram '''
	# obtaining values from 'data' for x1, and x2 being emission line fluxes where we define log(x1/x2) on the x-axis
	x_raw1, x_raw2 = data[x_raw1][:], data[x_raw2][:]
	x1, x2 = x_raw1[np.logical_not(x_raw1==0)], x_raw2[np.logical_not(x_raw1==0)] # removing row where fluxes equal 0
	# obtaining values from 'data' for y1, and y2 being emission line fluxes where we define log(y1/y2) on the y-axis
	y_raw1, y_raw2 = data[y_raw1][:], data[y_raw2][:]
	y1, y2 = y_raw1[np.logical_not(x_raw1==0)], y_raw2[np.logical_not(x_raw1==0)] # removing row where fluxes equal 0

	# obtaining values to be plotted in the VO87 diagram, being log(x1/x2) and log(y1/y2) on the x-axis and y-axis respectively
	x_ratio = np.log(np.array(x1) / np.array(x2))
	y_ratio = np.log(np.array(y1) / np.array(y2))
	return x_ratio, y_ratio

def ratio_class(data, x_raw1_name, x_raw2_name, y_raw1_name, y_raw2_name, table=False):
	''' Calculation of the values of the log(emission line ratios) while taking into account classifications obtained by VO87 diagram '''
	# obtaining values from 'data' for x1, and x2 being emission line fluxes where we define log(x1/x2) on the x-axis
	x_raw1, x_raw2, label_x = data[x_raw1_name][:], data[x_raw2_name][:], data['classification'][:]
	x1, x2, x_class = x_raw1[np.logical_not(x_raw1==0)], x_raw2[np.logical_not(x_raw1==0)], label_x[np.logical_not(x_raw1==0)]
	# obtaining values from 'data' for y1, and y2 being emission line fluxes where we define log(y1/y2) on the y-axis
	y_raw1, y_raw2, label_y = data[y_raw1_name][:], data[y_raw2_name][:], data['classification'][:]
	y1, y2, y_class = y_raw1[np.logical_not(x_raw1==0)], y_raw2[np.logical_not(x_raw1==0)], label_y[np.logical_not(x_raw1==0)]

	# obtaining values to be plotted in the emission line ratio diagram, being log(x1/x2) and log(y1/y2) on the x-axis and y-axis respectively
	x = np.log(np.array(x1) / np.array(x2))
	y = np.log(np.array(y1) / np.array(y2))

	# removing NaN values from the dataset
	x_ratio = x[~np.isnan(x)]
	x_class = x_class[~np.isnan(x)]
	y_ratio = y[~np.isnan(x)]
	
	x1, x2 = x1[~np.isnan(x)], x2[~np.isnan(x)]
	y1, y2 = y1[~np.isnan(x)], y2[~np.isnan(x)]

	# if table == True, the user is requested to give a table_name as input, where a table containing the original line fluxes, classifications acoording to the VO*& diagram and the line emission ratios on the x- and y-axis are imported into a table
	if table == True:
		table_name = input("\n ----------------------------------------------------------------------- \n                         You used table=True  \n !! put name emission line on x-axis in the tablename e.g.[O[ii]3729] !! \n tablename=  ")
		print("\n ----------------------------------------------------------------------- \n")
		
		# CREATE new_table, INSERT classification, x_ratio, y_ratio 
		new_table = Table()
		
		aa = Column(x_class, name='classification')
		new_table.add_column(aa, index=0)  # Insert before the first table column
		bb = Column(x_ratio, name='x_ratio')
		new_table.add_column(bb, index=1)  # Insert in second table column
		cc = Column(y_ratio, name='y_ratio')
		new_table.add_column(cc, index=2)  # Insert in third table column
		dd = Column(x1, name='%s' %(x_raw1_name))
		new_table.add_column(dd, index=3)  # Insert in fourth table column
		ee = Column(x2, name='%s' %(x_raw2_name))
		new_table.add_column(ee, index=4)  # Insert in fifth table column
		ff = Column(y1, name='%s' %(y_raw1_name))		
		new_table.add_column(ff, index=5)  # Insert in sixth table column
		
		# We do not import values for y2, since these are equal to the values of x2 (H_beta) for our classification purposes 
		#gg = Column(y2, name='%s' %(y_raw2_name))		
		#new_table.add_column(gg, index=5)  # Insert in sixth table column
		
		ascii.write(new_table, output='%s.csv' %(table_name), format='csv', overwrite=True)
		print("table %s.csv is stored in %s" %(table_name, pwd))
	return x_ratio, y_ratio, x_class, y_class

def plot_vo87(data, x_raw1, x_raw2, y_raw1, y_raw2, function, name='vo87'):
	''' Function to plot the VO87 diagram for log([N II]/Ha), log([S II]/Ha) or log([O I]/Ha) versus log([O III]/Hb) '''
	x_corr, y_corr = ratio(data, x_raw1, x_raw2, y_raw1, y_raw2)

	plt.figure(1, figsize=(6, 4))
	plt.plot(x_corr,y_corr, '+')
	if function == vo_line_n:
		plt.xlabel(r'$\log(N\lbrack ii\rbrack 6584/ H\alpha)$')
		plt.title(r'VO87 Diagram $N\lbrack ii\rbrack H\alpha$ vs. $O\lbrack iii\rbrack H\beta$')
		minx, maxx = -2.5, 0.25
		plt.xlim( minx, 1.0) 
		plt.hlines(np.log(3), minx, 1.0)
	if function == vo_line_s:
		plt.xlabel(r'$\log(S\lbrack ii\rbrack 6584/ H\alpha)$')
		plt.title(r'VO87 Diagram $S\lbrack ii\rbrack H\alpha$ vs. $O\lbrack iii\rbrack H\beta$')
		minx, maxx = -4.0, 0.05
		plt.xlim( minx, 0.5 ) 
		plt.hlines(np.log(3), minx, 0.5)
	if function == vo_line_o:
		plt.xlabel(r'$\log(O\lbrack i\rbrack 6584/ H\alpha)$')
		plt.title(r'VO87 Diagram $O\lbrack i\rbrack H\alpha$ vs. $O\lbrack iii\rbrack H\beta$')
		minx, maxx = -4.5, -0.8
		plt.xlim( minx, 0.0 ) 
		plt.hlines(np.log(3), minx, 0.0)
	x_function_plot = np.linspace(minx, maxx, 200)
	plt.plot(x_function_plot[:200],function(x_function_plot[:200]))
	plt.ylabel(r'$\log(O\lbrack iii\rbrack 5007/ H\beta)$')
	plt.ylim( -1.2, 1.5)  
	plt.savefig('plot%s.png' %name) 
	plt.show()
	plt.close()
	return

def plot_class(data, x_raw1, x_raw2, y_raw1, y_raw2, minx=-4.5, maxx=0.0, xline='no_line_input', yline='O[iii]5007 / H\beta', name='classification'):
	''' Function to plot an diagnostic diagram for log(x_raw1/x_raw2) versus log(y_raw1/y_raw2) with their classifications obtained by using the VO87 diagram obtained by the plot_vo87() function '''
	x_corr, y_corr, x_class, y_class = ratio_class(data, x_raw1, x_raw2, y_raw1, y_raw2)
	
	agn = [x_class=='AGN'] 							# find the emission line fluxes corresponding to AGN
	sbg = [x_class=='SBG']							# find the emission line fluxes corresponding to SBG
	
	plt.figure(1, figsize=(6, 4))
	plt.plot(x_corr[agn],y_corr[agn], 'b+')
	plt.plot(x_corr[sbg],y_corr[sbg], 'k+')
	plt.xlabel(r'log(%s$ / H\beta$)' %xline)
	plt.title(r'VO87 Diagram %s $H\beta$ vs. $O[iii] H\beta$' %xline)
	plt.xlim( minx, maxx )
	plt.ylabel(r'$\log(O[iii] 5007 / H\beta)$')
	plt.ylim( -1.2, 1.5)  
	plt.savefig('plot_class%s.png' %name) 
	plt.show()
	plt.close()
	return
