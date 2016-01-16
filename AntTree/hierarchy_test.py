# -*- coding:utf-8 -*-
import scipy as sp
import numpy as np
import scipy.spatial.distance as distance
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from random import random

n = 10
dim = 10
data = [[random() for i in range(dim)] for i in range(n)]
print 'data'
print data
result1 = linkage(data, method='single', metric='euclidean')
print 'result1'
print result1

dendrogram(result1)
plt.show()
