#!/usr/bin/python
from __future__ import unicode_literals
from __future__ import division

import sys
sys.path.append('/Users/users/mulder/astrods/project/plot_vo87')
import plot

import astropy
from astropy.io import fits, ascii

from astropy.table import Column

import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import datasets
from sklearn import svm

from matplotlib import pyplot as plt

data_table = astropy.io.ascii.read('/Users/users/mulder/astrods/project/sample_trainingsetwithclass.csv', format='csv')

x_ratio, y_ratio, x_class, y_class = plot.ratio_class(data_table, 'oii_3726_flux', 'h_beta_flux', 'oiii_5007_flux', 'h_beta_flux')

xy_ratio = []

for idx, j in enumerate(x_ratio):
	value = []
	value.append(x_ratio[idx])
	value.append(y_ratio[idx])
	xy_ratio.append(value)

xy_ratio = np.array(xy_ratio)
x_class = x_class[~np.isnan(xy_ratio).any(axis=1)]
xy_ratio = xy_ratio[~np.isnan(xy_ratio).any(axis=1)]	

X_train, X_test, label_train, label_test = train_test_split(xy_ratio, x_class, test_size=0.2, random_state=0)


''' SVC, NuSVC and LinearSVC are classes capable of performing multi-class classification on a dataset. '''


clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, xy_ratio, x_class, cv=5)
print(scores)


'''
clf = svm.SVC(kernel='linear', C=1).fit(X_train, label_train)
print(clf.score(X_test, label_test)  )    
'''



























