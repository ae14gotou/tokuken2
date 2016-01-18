# -*- coding:utf-8 -*-
import numpy as np

#クラスタの中心点(平均グラフ)を求める
def graph_average(dic):
    values = dic.values()
    tmp = values[0].copy()
    for i in range(len(values)-1):
        tmp +=  values[i+1]
        
    tmp = tmp / len(values)
    return tmp

#クラスタ内の二乗の総和
def squares_inCluster(data, k):
    Sum_K = 0.0
    for i in range(k):
        dic = data[i]
        values = dic.values()
        center = graph_average(data[i])
        #print 'center: ', center
        Sum = 0.0
        for j in range(len(values)):
            #print (center - values[j])**2
            Sum += sum((center - values[j])**2)
        Sum_K += Sum

    return Sum_K

#全データの二乗の総和
def squares_All(data, k):
    Sum_A = 0.0
    tmp = {}
    for i in range(k):
        tmp.update(data[i])
    a = tmp.values()
    #n = len(a)*len(a[0])
    n = len(a)
    #print n 
    center = graph_average(tmp)
    #print 'center: ',center
    
    for i in range(k):
        dic = data[i]
        values = dic.values()
        for j in range(len(values)):
            #print (center - values[j])**2
            #print Sum_A
            Sum_A += sum((center - values[j])**2)

    return Sum_A, n
    
def PseudoF(G, T, Pg, n):
    return ((T-Pg)/(G-1)) / (Pg/(n-G))

def main(data, k):
    Pg = squares_inCluster(data, k)
    T,n = squares_All(data, k)
    #print 'Pg: ',Pg
    #print 'T: ',T
    #print 'n: ',n
    #print 'k: ',k
    P_F = PseudoF(k, T, Pg, n)
    #print P_F
    return P_F

if __name__ == '__main__':
    #テスト用
    a = np.array([1.0,2.0,3.0,4.0,5.0])
    b = np.array([0.0,9.0,8.0,7.0,6.0])
    c = np.array([5.0,5.0,5.0,5.0,5.0])
    d = np.array([7.0,7.0,7.0,7.0,7.0])
    x = {100:a}#, 101:b}
    y = {200:c, 201:d}
    data = []
    data.append(x)
    data.append(y)
    print data
    main(data, 2)

    
