#!/usr/bin/env python3
# module load anaconda3/5.3.0

''' This pipeline is created in order to obtain/extract the moving objects from an CCD image 

1. Select and download one pair of images (i.e. for 1 CCD) from those listed above. Find the
observing dates, centers (RA,DEC) and dimension of the images. '''

import astropy
from astropy.io import fits, ascii

hdulist = fits.open("/Users/users/mulder/astrods/mandatory2/image1_ccd1.fits")
hdu = hdulist[0]
header = hdu.header

#print header en header keywords
ob_date = repr(header['DATE-OBS'])
ob_center_ra = repr(header['CRVAL1'])
ob_center_dec = repr(header['CRVAL2'])
ob_dim_x = repr(header['NAXIS1'])
ob_dim_y = repr(header['NAXIS2'])


'''
2. Open the images in your favorite image viewer. Align the images and blink them to identify
moving objects by eye. '''

aladin > open "/Users/users/mulder/astrods/mandatory2/image1_ccd1.fits"
aladin > open "/Users/users/mulder/astrods/mandatory2/image2_ccd1.fits"
aladin > Image_associations (1=image1_ccd1, 2=image2_ccd1), blink seq. -delay: 400ms


'''
3. Determine which characteristics of the moving objects make them stand out from other sources
(or close pairs of sources!), in addition to their motion. '''

sextractor > add "ELONGATION", "ELLIPTICITY" to default.param



'''
4. Perform source extraction. Ensure your output catalog contains parameters relevant for identifying
moving objects, considering step 3. '''

''' Using SEXtractor, extract sources from ccd image '''
import sewpy
sew = sewpy.SEW(params=["NUMBER", "FLUX_ISO", "FLUXERR_ISO", "MAG_ISO", "MAGERR_ISO", "MAG_ISOCOR", "MAGERR_ISOCOR", "MAG_APER(1)", "MAGERR_APER(1)", "MAG_AUTO", "MAGERR_AUTO", "MAG_BEST", "MAGERR_BEST", "X_IMAGE", "Y_IMAGE", "ALPHA_J2000", "DELTA_J2000", "A_IMAGE", "B_IMAGE", "ELONGATION", "ELLIPTICITY", "FLAGS"],
        config={"DETECT_MINAREA":6, "DETECT_THRESH":5})
out = sew("image1_ccd1.fits")
print (out["i1c1"])

# Or in command line

> sex -c sex.conf image1_ccd1.fits   # resulting in i1c1.cat



'''
5. Cross-match the sources in your two catalogs. Determine an appropriate matching radius (e.g.,
make use of your blinking exercise in step 2). '''

# In command line

> stilts tskymatch2 in1=i1c1.cat in2=i2c1.cat out=crossid_ccd1.csv ra1=ALPHA_J2000 dec1=DELTA_J2000 ra2=ALPHA_J2000 dec2=DELTA_J2000 error=2.5



'''
6. Identify high proper motion candidates and write a procedure to filter these out automatically using
the source parameters in your (matched) catalog(s). '''

from astropy.table import Table

ccd1 = ascii.read("/Users/users/mulder/astrods/mandatory2/minearea6thresh5/crossid_ccd1.csv", format='csv', fast_reader=False)
mask1 = (ccd1['ELONGATION_1'] > 2.6) & (ccd1['ELONGATION_2'] > 2.6) # & (ccd1['SEPERATION'] > 2.0)
m_obj1 = (ccd1[mask1])
ascii.write(m_obj1, 'm_obj1.csv', format='csv', fast_writer=True)



'''
7. Use http://vo.imcce.fr/webservices/skybot/?forms to determine if any of the moving objects are known
Solar System objects.    '''

# For all objects found in crossid_ccd1.csv
skybot > Epoch (UTC): 2013-02-18T08:04:55
skybot > Target: 182.867502957 -1.90180718003
skybot > Objects: Asteroids, Planets, Comets
skybot > Radius (arcsec): 2
skybot > Observer: 309                          # Paranal
skybot > Filter: 120                            # Maximum position error
skybot > Output: Object






'''
ccd1 = ascii.read("/Users/users/mulder/astrods/mandatory2/minearea6thresh5/crossid_ccd1.csv", format='csv', fast_reader=False)
ccd2 = ascii.read("/Users/users/mulder/astrods/mandatory2/minearea6thresh5/crossid_ccd2.csv", format='csv', fast_reader=False)
ccd3 = ascii.read("/Users/users/mulder/astrods/mandatory2/minearea6thresh5/crossid_ccd3.csv", format='csv', fast_reader=False)
ccd4 = ascii.read("/Users/users/mulder/astrods/mandatory2/minearea6thresh5/crossid_ccd4.csv", format='csv', fast_reader=False)
ccd5 = ascii.read("/Users/users/mulder/astrods/mandatory2/minearea6thresh5/crossid_ccd5.csv", format='csv', fast_reader=False)

mask1 = (ccd1['ELONGATION_1'] > 2.6) & (ccd1['ELONGATION_2'] > 2.6) # & (ccd1['SEPERATION'] > 2.0)
mask2 = (ccd2['ELONGATION_1'] > 2.6) & (ccd2['ELONGATION_2'] > 2.6) # & (ccd2['SEPERATION'] > 2.0)
mask3 = (ccd3['ELONGATION_1'] > 2.6) & (ccd3['ELONGATION_2'] > 2.6) # & (ccd3['SEPERATION'] > 2.0)
mask4 = (ccd4['ELONGATION_1'] > 2.6) & (ccd4['ELONGATION_2'] > 2.6) # & (ccd4['SEPERATION'] > 2.0)
mask5 = (ccd5['ELONGATION_1'] > 2.6) & (ccd5['ELONGATION_2'] > 2.6) # & (ccd5['SEPERATION'] > 2.0)


m_obj1 = (ccd1[mask1])
m_obj2 = (ccd2[mask2])
m_obj3 = (ccd3[mask3])
m_obj4 = (ccd4[mask4])
m_obj5 = (ccd5[mask5])

ascii.write(m_obj1, 'm_obj1.csv', format='csv', fast_writer=True)
ascii.write(m_obj2, 'm_obj2.csv', format='csv', fast_writer=True)
ascii.write(m_obj3, 'm_obj3.csv', format='csv', fast_writer=True)
ascii.write(m_obj4, 'm_obj4.csv', format='csv', fast_writer=True)
ascii.write(m_obj5, 'm_obj5.csv', format='csv', fast_writer=True)


print ("CCD1")
print (m_obj1["ALPHA_J2000_1", "DELTA_J2000_1", "ALPHA_J2000_2", "DELTA_J2000_2"])
print ("CCD2")
print (m_obj2["ALPHA_J2000_1", "DELTA_J2000_1", "ALPHA_J2000_2", "DELTA_J2000_2"])
print ("CCD3")
print (m_obj3["ALPHA_J2000_1", "DELTA_J2000_1", "ALPHA_J2000_2", "DELTA_J2000_2"])
print ("CCD4")
print (m_obj4["ALPHA_J2000_1", "DELTA_J2000_1", "ALPHA_J2000_2", "DELTA_J2000_2"])
print ("CCD5")
print (m_obj5["ALPHA_J2000_1", "DELTA_J2000_1", "ALPHA_J2000_2", "DELTA_J2000_2"])
'''









'''
# Connecting to the MariaDB via SQL ect.
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(host='localhost', user='root', password='', database='moving_sources')
cursor = mariadb_connection.cursor()

#cursor.execute("DROP TABLE cm2;")
cursor.execute("CREATE TABLE test;")
cursor.execute("LOAD DATA LOCAL INFILE "/Users/users/mulder/astrods/mandatory2/minearea6thresh5/crossid.csv" INTO TABLE moving_sources.table FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n';")
'''



