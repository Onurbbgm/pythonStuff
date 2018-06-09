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
#print(X_scaled)

import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
#data = pd.read_json('resultOscarsUserAna2.json')
data = pd.read_json('usersInfoInfluence.json') #com nivel popularidade
print(data)
UsersId = data["idUser"].values
TotalLikes = data["total_likes"].values
AverageLikes = data["average_likes"].values
RetweetCountTotal =  data["retweet_count_total"].values
AverageRetweet = data["average_retweet_count"].values
ImportantDataForInfluencer = data[["average_retweet_count","average_likes"]].values
#Popular user make calculation
InfluenceLevel = data["influence_level"].values
FollowersCount = data["followers_count"].values
FinalFollowersCount = data["final_followers_count"].values
FollowersIdUser = data[["idUser","followers_count"]].values
#Clustering
clus = KMeans(n_clusters=2).fit(FollowersIdUser)
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
from sklearn.naive_bayes import MultinomialNB
#clf = BernoulliNB()
clf = MultinomialNB()
clf.fit(ImportantDataForInfluencer, InfluenceLevel)
BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
print("Predict popularity according to average likes and average retweets using MultinomialNB")
pred = clf.predict(ImportantDataForInfluencer)
print(pred)
#pandaPred = pred.toPandas()
#pred.to_json()
#predJson = pd.read_csv()
file = open("C:/Users/Bruno/Desktop/PUC/TCC 2/python-twitter-master/examples/influenciaPredict.txt", "a+")
for preds in pred:
    file.write(str(preds) +"\n")

#for s in pred:
 #   print(s)
print("Predict Probabilidade")
print(clf.predict_proba(ImportantDataForInfluencer))
print("Popular pos...")
print(InfluenceLevel)
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
#dataNum = vec.fit_transform(SomeData).toarray()
#print(dataNum)


