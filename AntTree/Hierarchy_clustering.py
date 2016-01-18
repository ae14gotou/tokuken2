# -*- coding:utf-8 -*-
import scipy as sp
import numpy as np
import pandas as pd
import scipy.spatial.distance as distance
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from random import random

#dendrogramの戻り値を利用しデータにラベルを与える
def set_label(Y, X, result, codes):
    color_list = Y['color_list']
    tmp = []
    #色の数=クラスタの数（とする）
    for i in color_list:
        if i in tmp: pass
        else:
            tmp.append(i)
    #print tmp

    r_tmp = [] #return値を格納する配列
    for i in tmp:
        dic = {}
        for j in range(len(color_list)):
            if i == color_list[j]:
                n1 = int(result[j][0]) #indexのためint型
                n2 = int(result[j][1])
                
                if n1 < len(codes):
                    dic[codes[n1]] = X[n1]
                    
                else : pass
                if n2 < len(codes):
                    dic[codes[n2]] = X[n2]
                    
                else : pass
            else : pass
        r_tmp.append(dic)
     
    return r_tmp

def main(fname1, fname2, m):
    data = pd.read_csv(fname1)
    codes = pd.read_csv(fname2)
    #print codes
    t = []  #会社コードの順番
    for i in codes.values:
        t.append(i[0])

    X = data.values
    #method=手法の種類,metric=ユークリッド距離
    result = linkage(X, method=m, metric='euclidean')   
    Y = dendrogram(result, labels=t)
    #linkage,dendrogramの戻り値等はScipy.orgのサイト参照
    return_dic = set_label(Y, X, result, t)
    #plt.title('Result dendrogram')
    #plt.show()

    return return_dic

if __name__ == "__main__":
    fname1 = 'return_index_values.csv'
    fname2 = 'return_index_codes.csv'
    r = main(fname1, fname2, 'single')
    

