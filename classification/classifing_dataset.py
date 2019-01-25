import sys
sys.path.append('/Users/users/mulder/astrods/project/plot_vo87')
import plot

import astropy
from astropy.io import fits, ascii

from astropy.table import Column

import numpy as np

data_table = astropy.io.ascii.read('/Users/users/mulder/astrods/project/sample_trainingset.csv', format='csv')

vo_n_xmax = (0.61/(-1.4-1.19))+0.47
vo_s_xmax = (0.72/(-1.4-1.30))+0.32
vo_o_xmax = (0.73/(-1.4-1.33))-0.59

x_theory = np.linspace(-0.4, vo_n_xmax, 200)
x_real, y_real = plot.ratio(data_table,'nii_6584_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux')

new_column = []
for i in range(len(x_real)):					# for all values check if they lie below or above semiemperical line defined by vo_line_X, where X is n[ii], s[ii] or o[i]
	if y_real[i] > plot.vo_line_n(x_real[i]) or x_real[i] > 0.3:	
		new_column.append('AGN') 							# below semiemperical line are classified as 'galaxies hosting an AGN'
	else: 
		new_column.append('SBG')							# above semiemperical line galaxies are classified as 'Starburst galaxies'

aa = Column(new_column, name='classification')
data_table.add_column(aa, index=0)  # Insert before the first table column

ascii.write(data_table, output='/Users/users/mulder/astrods/project/sample_trainingsetwithclass.csv', format='csv', overwrite=True)

'''
plot.plot_vo87(data,'nii_6584_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', plot.vo_line_n, name='nii_test')
plot_vo87(data,'nii_6584_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_n, name='nii')
plot_vo87(data,'sii_6717_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_s, name='sii')
plot_vo87(data,'oi_6300_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_o, name='oi')

h_beta_flux
oii_3729_flux
oii_3726_flux
oiii_4959_flux
oiii_5007_flux
'''
