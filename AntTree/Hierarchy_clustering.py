# -*- coding:utf-8 -*-
import scipy as sp
import numpy as np
import pandas as pd
import scipy.spatial.distance as distance
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from random import random

def set_label(Y, X):
    color_list = Y['color_list']
    codes = Y['ivl']

def main(fname1, fname2, m):
    data = pd.read_csv(fname1)
    codes = pd.read_csv(fname2)
    print codes
    t = []
    for i in codes.values:
        t.append(i[0])

    X = data.values
    result1 = linkage(X, method=m, metric='euclidean')   
    print result1

    Y = dendrogram(result1, labels=t)
    plt.show()

    print Y

if __name__ == "__main__":
    fname1 = 'return_index_values.csv'
    fname2 = 'return_index_codes.csv'
    main(fname1, fname2, 'single')
    
'''
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
'''
