import plot

import astropy
from astropy.io import fits, ascii

data = astropy.io.ascii.read('/Users/users/mulder/astrods/project/sample_trainingsetwithclass.csv',format='csv', fast_reader=False)        #sample_oldlines.csv')


''' format:  minx=-4.5, maxx=0.0, xline='O[ii]3726/ H\alpha', yline='O[iii]5007 / H\beta', name='classification'  '''
plot.plot_class(data,'nii_6584_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', minx=-4.5, maxx=2.0, xline='N[ii]5684', name='_n[ii]6584')    
#plot.plot_class(data,'oii_3726_flux', 'h_beta_flux', 'oiii_5007_flux', 'h_beta_flux', minx=-4.5, maxx=2.0, xline='O[ii]3726', name='_O[ii]3726')    
#plot.plot_class(data, 'oii_3729_flux', 'h_beta_flux', 'oiii_5007_flux', 'h_beta_flux', minx=-4.5, maxx=2.0, xline='O[ii]3729', name='_O[ii]3729')


'''
lines needed to create the project training dataset

plot_vo87(data,'nii_6584_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_n, name='nii')
plot_vo87(data,'sii_6717_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_s, name='sii')
plot_vo87(data,'oi_6300_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_o, name='oi')
'''

''' 
lines needed for project classification:

h_beta_flux
oii_3729_flux
oii_3726_flux
oiii_4959_flux
oiii_5007_flux
'''
