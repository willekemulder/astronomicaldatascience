import astropy
from astropy.io import fits, ascii

import numpy as np

from astroquery.sdss import SDSS
from astropy import coordinates as coords

query = "SELECT s.plate, s.fiberid, s.mjd, s.z, s.zwarning, nii_6584_flux, nii_6584_flux_err, g.h_beta_flux, g.h_beta_flux_err, g.h_alpha_flux, g.h_alpha_flux_err, g.oii_3729_flux, g.oii_3729_flux_err, g.oii_3726_flux, g.oii_3726_flux_err, g.oiii_4959_flux, g.oiii_4959_flux_err, g.oiii_5007_flux, g.oiii_5007_flux_err  FROM GalSpecLine AS g  JOIN SpecObj AS s  ON s.specobjid = g.specobjid  WHERE  h_alpha_flux > h_alpha_flux_err*5  AND h_beta_flux > h_beta_flux_err*5  AND h_beta_flux_err > 0  AND h_alpha_flux > 10.*h_beta_flux  AND s.class = 'GALAXY'  AND s.zwarning = 0 "
sample_n = SDSS.query_sql(query)
ascii.write(sample_n, output='/Users/users/mulder/astrods/project/sample_trainingset.csv', format='csv', overwrite=True)            #sample_newlines.csv', format='csv', overwrite=True)




'''
#query = "SELECT s.plate, s.fiberid, s.mjd, s.z, s.zwarning, g.h_beta_flux, g.h_beta_flux_err, g.oii_3729_flux, g.oii_3729_flux_err, g.oii_3726_flux, g.oii_3726_flux_err, g.oiii_4959_flux, g.oiii_4959_flux_err, g.oiii_5007_flux, g.oiii_5007_flux_err  FROM GalSpecLine AS g  JOIN SpecObj AS s  ON s.specobjid = g.specobjid  WHERE  h_alpha_flux > h_alpha_flux_err*5  AND h_beta_flux > h_beta_flux_err*5  AND h_beta_flux_err > 0  AND h_alpha_flux > 10.*h_beta_flux  AND s.class = 'GALAXY'  AND s.zwarning = 0 "



#query = "SELECT s.plate, s.fiberid, s.mjd, s.z, s.zwarning, g.h_beta_flux, g.h_beta_flux_err, g.h_alpha_flux, g.h_alpha_flux_err, nii_6584_flux, nii_6584_flux_err, sii_6717_flux, sii_6717_flux_err, oi_6300_flux, oi_6300_flux_err, g.oiii_5007_flux, g.oiii_5007_flux_err  FROM GalSpecLine AS g  JOIN SpecObj AS s  ON s.specobjid = g.specobjid  WHERE  h_alpha_flux > h_alpha_flux_err*5  AND h_beta_flux > h_beta_flux_err*5  AND h_beta_flux_err > 0  AND h_alpha_flux > 10.*h_beta_flux  AND s.class = 'GALAXY'  AND s.zwarning = 0 "
#sample_o = SDSS.query_sql(query)
#ascii.write(sample_o, output='/Users/users/mulder/astrods/project/sample_oldlines.csv', format='csv', overwrite=True)
'''
