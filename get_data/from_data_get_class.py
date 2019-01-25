import sys
sys.path.append('/Users/users/mulder/astrods/projectgit/plot_vo87')
import plot

import astropy
from astropy.io import fits, ascii

import numpy as np

from astroquery.sdss import SDSS
from astropy import coordinates as coords

data = astropy.io.ascii.read('/Users/users/mulder/astrods/project/sample_trainingsetwithclass.csv',format='csv', fast_reader=False)
plot.ratio_class(data, 'oii_3726_flux', 'h_beta_flux', 'oiii_5007_flux', 'h_beta_flux', table=True)
plot.ratio_class(data, 'oii_3729_flux', 'h_beta_flux', 'oiii_5007_flux', 'h_beta_flux', table=True)
