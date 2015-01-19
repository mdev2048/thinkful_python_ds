#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
The Iris Dataset
=========================================================
This data sets consists of 3 different types of irises'
(Setosa, Versicolour, and Virginica) petal and sepal
length, stored in a 150x4 numpy.ndarray

The rows being the samples and the columns being:
Sepal Length, Sepal Width, Petal Length	and Petal Width.

The below plot uses the first two features.
See `here <http://en.wikipedia.org/wiki/Iris_flower_data_set>`_ for more
information on this dataset.
"""
print(__doc__)

def most_common(lst):
    return max(set(lst), key=lst.count)
# Code source: GaÃ«l Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import random
import math


# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()

# Pick a new point, programmatically at random.
x_random = x_max * random.random()
y_random = y_max * random.random()

new_point = [x_random, y_random]
    
sorted_list = [[X[i][0],X[i][1],iris.target[i]] for i in range(0,len(X))]
# Sort each point by its distance from the new point, and subset the 10 nearest points.
def distance(p1):
	p0 = new_point
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

sorted_list = sorted(sorted_list, key=distance)

print "new point",new_point



# # Determine the majority class of the subset.
print "most common class", most_common([el[2] for el in sorted_list[:10]])
 

# for curItem in sorted_list[:10]:
# 	print X.index(curItem)
    

# See if you can write a function called knn() that will take k as an argument and return the majority class for different values of k.
def manual_knn(k):
	sorted_list = sorted([[X[i][0],X[i][1],iris.target[i]] for i in range(0,len(X))], key=distance)
	return most_common([el[2] for el in sorted_list][:k])

def auto_knn(k):
	# is this suppose to return the order of classes of nearest neighbors?
	neigh = KNeighborsClassifier(n_neighbors=k)
	return neigh.fit(X,Y).predict(X)

# trying for k=6
print "manual",manual_knn(6)
print "auto", auto_knn(6)





