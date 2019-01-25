

import astropy
from astropy.io import fits, ascii

import numpy as np

from astroquery.sdss import SDSS
from astropy import coordinates as coords

#pos = coords.SkyCoord('0h8m05.63s +14d50m23.3s', frame='icrs')
#xid = SDSS.query_region(pos, spectro=True)
#sp = SDSS.get_spectra(matches=xid)

#hdulist = pf.open(sp)
#c0 = hdulist[0].header['coeff0']
#c1 = hdulist[0].header['coeff1']
#npix = hdulist[0].header['naxis1']

#s = SDSS.get_spectra_async(plate=5177, mjd=56245, fiberID=114)

print('check1')

query = "SELECT s.plate, s.fiberid, s.mjd, s.z, s.zwarning, g.h_beta_flux, g.h_beta_flux_err, g.oii_3729_flux, g.oii_3729_flux_err, g.oii_3726_flux, g.oii_3726_flux_err, g.oiii_4959_flux, g.oiii_4959_flux_err, g.oiii_5007_flux, g.oiii_5007_flux_err  FROM GalSpecLine AS g  JOIN SpecObj AS s  ON s.specobjid = g.specobjid  WHERE  h_alpha_flux > h_alpha_flux_err*5  AND h_beta_flux > h_beta_flux_err*5  AND h_beta_flux_err > 0  AND h_alpha_flux > 10.*h_beta_flux  AND s.class = 'GALAXY'  AND s.zwarning = 0 "
sample_n = SDSS.query_sql(query)
ascii.write(sample_n, output='sample_newlines.csv', format='csv')

query = "SELECT s.plate, s.fiberid, s.mjd, s.z, s.zwarning, g.h_beta_flux, g.h_beta_flux_err, g.h_alpha_flux, g.h_alpha_flux_err, nii_6584_flux, nii_6584_flux_err, sii_6717_flux, sii_6717_flux_err, oi_6300_flux, oi_6300_flux_err, g.oiii_5007_flux, g.oiii_5007_flux_err  FROM GalSpecLine AS g  JOIN SpecObj AS s  ON s.specobjid = g.specobjid  WHERE  h_alpha_flux > h_alpha_flux_err*5  AND h_beta_flux > h_beta_flux_err*5  AND h_beta_flux_err > 0  AND h_alpha_flux > 10.*h_beta_flux  AND s.class = 'GALAXY'  AND s.zwarning = 0 "
sample_o = SDSS.query_sql(query)
ascii.write(sample_o, output='sample_oldlines.csv', format='csv')

print('check2')





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
