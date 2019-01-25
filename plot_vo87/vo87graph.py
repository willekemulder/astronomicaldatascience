import plot
import astropy
from astropy.io import fits, ascii

data = astropy.io.ascii.read('/Users/users/mulder/astrods/project/sample_trainingset.csv')        #sample_oldlines.csv')

plot.plot_vo87(data,'nii_6584_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', plot.vo_line_n, name='nii_trainingset')


# lines needed for project training dataset

#plot_vo87(data,'nii_6584_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_n, name='nii')
#plot_vo87(data,'sii_6717_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_s, name='sii')
#plot_vo87(data,'oi_6300_flux', 'h_alpha_flux', 'oiii_5007_flux', 'h_beta_flux', vo_line_o, name='oi')


# lines needed for project classification
#h_beta_flux
#oii_3729_flux
#oii_3726_flux
#oiii_4959_flux
#oiii_5007_flux
