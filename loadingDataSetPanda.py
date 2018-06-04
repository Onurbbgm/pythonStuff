# -*- coding: utf-8 -*-
"""
Created on Tue May 29 00:18:24 2018

@author: Bruno
"""

from sklearn import preprocessing
import numpy as np
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])
X_scaled = preprocessing.scale(X)
print(X_scaled)

import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
#data = pd.read_json('resultOscarsUserAna2.json')
data = pd.read_json('resultOscarsUserAna3.json') #com nivel popularidade
print(data)
UsersId = data["idUser"].values
Likes = data["likes"].values
RetweetCount =  data["retweet_count"].values
SomeData = data[["retweet_count","likes","followers_count"]].values
#Popular user make calculation
Popular = data["nivel_popularidade"].values
OtherData = data[["likes","idUser"]].values
FollowersCount = data["followers_count"].values
Text = data["text_content"].values
#Clustering
clus = KMeans(n_clusters=2).fit(OtherData)
print("Clustering")
print(clus)
centers = clus.cluster_centers_;
print("Centerss:")
print(centers)
labels = clus.labels_;
print("Labels:")
print(labels)
#print(UsersId)
#UsersId.astype(float)
#print(preprocessing.scale(UsersId))
#Predicting
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf.fit(SomeData, Popular)
BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
print("Predict popularity according to likes, retweets and followers")
pred = clf.predict(SomeData)
print(pred)
#for s in pred:
 #   print(s)
print("Predict Probabilidade")
print(clf.predict_proba(SomeData))

from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
#dataNum = vec.fit_transform(SomeData).toarray()
#print(dataNum)
























#is not necessary
'''pd.read_json('resultOscarsUserAna2.json', dtype={'id':'string', 
                                           'idUser':'string',
                                           'date_time':'string',
                                           'hashtags':'string',
                                           'retweet':'string',
                                           'retweet_count': 'int',
                                           'followers_count': 'int',
                                           'likes': 'int',
                                           'text_content': 'string'})'''