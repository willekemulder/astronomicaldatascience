import astropy
from astropy.io import fits, ascii

import numpy as np

from astroquery.sdss import SDSS
from astropy import coordinates as coords

data = astropy.io.ascii.read('/Users/users/mulder/astrods/projectgit/datatables/o3729_withoriginaldata+class.csv',format='csv', fast_reader=False)
print(data)

from astropy.io.votable import from_table, writeto
votable = from_table(data)
writeto(votable, '/Users/users/mulder/astrods/projectgit/datatables/o3729.xml')

import pandas as pd
df = pd.read_csv('/Users/users/mulder/astrods/projectgit/datatables/o3729_withoriginaldata+class.csv')
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
        <FIELD ID="x_ratio" datatype="double" name="x_ratio"/>
        <FIELD ID="y_ratio" datatype="double" name="y_ratio"/>
        <FIELD ID="oii_3729_flux" datatype="double" name="oii_3726_flux"/>
        <FIELD ID="h_beta_flux" datatype="double" name="h_beta_flux"/>
        <FIELD ID="oiii_5007_flux" datatype="double" name="oiii_5007_flux"/>
        <FIELD ID="class_line" arraysize="3" datatype="unicodeChar" name="class_line"/>
		  <DESCRIPTION>Determined by using the VO87 diagnostic plot using Python</DESCRIPTION>
        <FIELD ID="class_knn1" arraysize="3" datatype="unicodeChar" name="class_knn1"/>
		  <DESCRIPTION>Determined by using the klaR package of the computer language R</DESCRIPTION>
        <FIELD ID="class_knn3" arraysize="3" datatype="unicodeChar" name="class_knn3"/>
		  <DESCRIPTION>Determined by using the klaR package of the computer language R</DESCRIPTION>
        <FIELD ID="class_lda" arraysize="3" datatype="unicodeChar" name="class_lda"/>
		  <DESCRIPTION>Determined by using the klaR package of the computer language R</DESCRIPTION>
        <FIELD ID="class_qda" arraysize="3" datatype="unicodeChar" name="class_qda"/>
		  <DESCRIPTION>Determined by using the klaR package of the computer language R</DESCRIPTION>
        </FIELD>
        <DATA>
          <TABLEDATA>""" %(resource_name, table_name, description) 


def convert_row(row):
    return """          <TR>
            <TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD><TD>%s</TD>
          <TR>""" % ( 
	row.x_ratio, row.y_ratio, row.oii_3729_flux, row.h_beta_flux, row.oiii_5007_flux, row.class_line, row.class_knn1, row.class_knn3, row.class_lda, row.class_qda)

    
def convert_endinfo():
	return """          </TABLEDATA>
        </DATA>
      </TABLE>
    </RESOURCE>
</VOTABLE> """ 

print(convert_info('myClassification', 'results', 'Classification of AGN and SBG galaxies based on KNN, LDA and QDA classifiers'))
print('\n'.join(df.apply(convert_row, axis=1)))
print(convert_endinfo())
