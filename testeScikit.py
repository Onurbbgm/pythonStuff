# -*- coding: utf-8 -*-
"""
Created on Wed May 16 23:11:42 2018

@author: Bruno
"""

from sklearn import cluster, datasets
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris) 
#KMeans(algorithm='auto', copy_x=True, init='k-means++')
print(k_means.labels_[::10])
#[1 1 1 1 1 0 0 0 0 0 2 2 2 2 2]
print(y_iris[::10])
#[0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]