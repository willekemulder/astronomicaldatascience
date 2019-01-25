import astropy
from astropy.io import fits, ascii

import numpy as np

from astroquery.sdss import SDSS
from astropy import coordinates as coords

data = astropy.io.ascii.read('/Users/users/mulder/astrods/projectgit/sample_trainingsetwithclass.csv',format='csv', fast_reader=False)
print(data)

from astropy.io.votable import from_table, writeto
votable = from_table(data)
writeto(votable, 'o3726.xml')

import pandas as pd
df = pd.read_csv('/Users/users/mulder/astrods/projectgit/sample_trainingsetwithclass.csv')
print(df)


def convert_info(resource_name, table_name, description):
	return """ <?xml version="1.0"?>
  <VOTABLE version="1.3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://www.ivoa.net/xml/VOTable/v1.3"
  xmlns:stc="http://www.ivoa.net/xml/STC/v1.30" >
    <RESOURCE name="%s">
      <TABLE name="%s">
        <DESCRIPTION>"%s"</DESCRIPTION>
        <GROUP utype="stc:CatalogEntryLocation">
          <PARAM name="href" datatype="char" arraysize="*"
            utype="stc:AstroCoordSystem.href" value="ivo://STClib/CoordSys#UTC-ICRS-TOPO"/>
          <PARAM name="URI" datatype="char" arraysize="*"
            utype="stc:DataModel.URI" value="http://www.ivoa.net/xml/STC/stc-v1.30.xsd"/>
          <FIELDref utype="stc:AstroCoords.Position2D.Value2.C1" ref="col1"/>
          <FIELDref utype="stc:AstroCoords.Position2D.Value2.C2" ref="col2"/>
        </GROUP>
        <FIELD ID="classification" arraysize="3" 
          datatype="unicodeChar" name="Classification"/>
        <FIELD ID="plate" datatype="long" name="plate"/>
        <FIELD ID="fiberid" datatype="long" name="fiberid"/>
        <FIELD ID="mjd" datatype="long" name="mjd"/>
        <FIELD ID="z" datatype="double" name="z"/>
          <DESCRIPTION>Distance of Galaxy, assuming H=75km/s/Mpc</DESCRIPTION>
        <FIELD ID="h_beta_flux" datatype="double" name="h_beta_flux"/>
        <FIELD ID="h_beta_flux_err" datatype="double" name="h_beta_flux_err"/>
        <FIELD ID="oii_3726_flux" datatype="double" name="oii_3726_flux"/>
        <FIELD ID="oii_3726_flux_err" datatype="double" name="oii_3726_flux_err"/>
        <FIELD ID="oii_3729_flux" datatype="double" name="oii_3729_flux"/>
        <FIELD ID="oii_3729_flux_err" datatype="double" name="oii_3729_flux_err"/>
        <FIELD ID="oiii_5007_flux" datatype="double" name="oiii_5007_flux"/>
        <FIELD ID="oiii_5007_flux_err" datatype="double" name="oiii_5007_flux_err"/>
        </FIELD>
        <DATA>
          <TABLEDATA>""" %(resource_name, table_name, description) 


def convert_row(row):
    return """          <TR>
            <TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD>
          <TR>""" % ( 
	row.classification, row.plate, row.fiberid, row.mjd, row.z, row.h_beta_flux, row.h_beta_flux_err, row.oii_3726_flux, row.oii_3726_flux_err, row.oii_3729_flux, row.oii_3729_flux_err, row.oiii_5007_flux, row.oiii_5007_flux_err)

    
def convert_endinfo():
	return """          </TABLEDATA>
        </DATA>
      </TABLE>
    </RESOURCE>
</VOTABLE> """ 

print(convert_info('myClassification', 'results', 'Classification of AGN and SBG galaxies based on KNN, LDA and QDA classifiers'))
print('\n'.join(df.apply(convert_row, axis=1)))
print(convert_endinfo())
