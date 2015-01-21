# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:30:54 2015
@author: sroy
"""

import pandas as pd
from os.path import join
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB


df  = pd.read_csv('ideal_weight.csv', names=['id', 'sex', 'actual', 'ideal', 'diff'], header=0)
df['sex'] = df['sex'].map(lambda x: x.replace("'",""))


plt.figure()
plt.hist([df['actual'], df['ideal']], histtype='bar', stacked=False)
plt.show()

# Convert into categorical variable
df['gender'] = pd.Categorical(df['sex'].tolist())


gnb = GaussianNB()
data = df[['actual','ideal','diff']]
target = df['gender']
gnb_fit = gnb.fit(data, target)
y_pred = gnb_fit.predict(data)

num_mismatch = 0
for i in range(0,len(target)):
	if target[i] != y_pred[i]:
		num_mismatch += 1
print("Number of mislabeled points out of a total %d points: %d" %(data.shape[0], num_mismatch))

# Predict the sex for an actual weight of 145, an ideal weight of 160, and a diff of -15.
print gnb_fit.predict([145,160,-15])

# Predict the sex for an actual weight of 160, an ideal weight of 145, and a diff of 15.
print gnb_fit.predict([160,140,15])