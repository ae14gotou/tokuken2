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
        Sum = 0.0
        for j in range(len(values)):
            Sum += sum((center - values[j])**2)
        Sum_K += Sum

    return Sum_K
          
def PseudoF(G, T, Pg, n):
    return ((T-Pg)/(G-1)) / (Pg/(n-G))

def main(data, k):
    Pg = squares_inCluster(data, k)
    T = 
#if __name__ == '__main__':

    
