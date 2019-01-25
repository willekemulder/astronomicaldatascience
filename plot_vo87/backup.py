from __future__ import unicode_literals


import astropy
from astropy.io import fits, ascii

from astroquery.sdss import SDSS
from astropy import coordinates as coords


import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
from matplotlib import pyplot as plt


data = astropy.io.ascii.read('/Users/users/mulder/astrods/project/sample_oldlines.csv')











def plot_vo87(data, corrx1, corrx2, corry1, corry2):

x1 = data['nii_6584_flux'][:]  			# nii_6584_flux - h_alpha_flux
x2 = data['h_alpha_flux'][:]  			# nii_6584_flux - h_alpha_flux

y1 = data['oiii_5007_flux'][:]   		# oiii_5007_flux - h_beta_flux
y2 = data['h_beta_flux'][:]   			# oiii_5007_flux - h_beta_flux

x_data = np.log(np.array(x1) / np.array(x2))
y_data = np.log(np.array(y1) / np.array(y2))

#VO87 Diagram from http://iopscience.iop.org/article/10.1086/318944/pdf (5, 6, 7)

def vo_line_n(x):
	y = (0.61/(x - 0.47))+1.19
	y = 10**y
	return y

def vo_line_s(x):
	y = (0.72/(x - 0.32))+1.30
	y = 10**y
	return y

def vo_line_o(x):
	y = (0.73/(x - 0.59))+1.33
	y = 10**y
	return y

x_plot = np.linspace(np.min(x_data), np.max(x_data), 200)

plt.figure(1, figsize=(6, 4))
plt.plot(x_data,y_data, '+')
plt.plot(x_plot[:190],vo_line_n(x_plot[:190]))
plt.xlabel(r'$N\lbrack ii\rbrack 6584/ H\alpha$')
plt.ylabel(r'$O\lbrack iii\rbrack 5007/ H\beta$')
plt.title(r'VO87 Diagram $N\lbrack ii\rbrack vs. O\lbrack iii\rbrack$')
plt.show()

plt.figure(1, figsize=(6, 4))
plt.plot(x_data,y_data, '+')
plt.plot(x_plot[:190],vo_line_n(x_plot[:190]))
plt.xlabel(r'$N\lbrack ii\rbrack 6584/ H\alpha$')
plt.ylabel(r'$O\lbrack iii\rbrack 5007/ H\beta$')
plt.title(r'VO87 Diagram $N\lbrack ii\rbrack vs. O\lbrack iii\rbrack$')
plt.show()

plt.figure(1, figsize=(6, 4))
plt.plot(x_data,y_data, '+')
plt.plot(x_plot[:190],vo_line_n(x_plot[:190]))
plt.xlabel(r'$N\lbrack ii\rbrack 6584/ H\alpha$')
plt.ylabel(r'$O\lbrack iii\rbrack 5007/ H\beta$')
plt.title(r'VO87 Diagram $N\lbrack ii\rbrack vs. O\lbrack iii\rbrack$')
plt.show()



#h_beta_flux
#oii_3729_flux
#oii_3726_flux
#oiii_4959_flux
#oiii_5007_flux






#wigglez = ascii.read("/Users/users/mulder/astrods/project/wigglez.dat")#, format='csv', fast_reader=False)

#print(wigglez.colnames)

#hdulist = fits.open("/Users/users/mulder/astrods/mandatory2/image1_ccd1.fits")
#hdu = hdulist[0]
#header = hdu.header
