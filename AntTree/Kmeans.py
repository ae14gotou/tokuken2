#coding:utf-8
import numpy as np
import pandas as pd
import scipy.cluster
from pylab import *

def show_plot(code, X):
    # 各データをクラスタ別に色分けして描画
        for i in range(len(X)):
            x1, x2 = X[i, ]

            if code[i] == 0: color = 'r+'
            elif code[i] == 1: color = 'b+'
            elif code[i] == 2: color = 'g+'
            elif code[i] == 3: color = 'm+'
            else : color = 'c+'
            plot(x1, x2, color)

        # セントロイドを描画
        #x1, x2 = np.transpose(codebook)
        #plot(x1, x2, 'wo')

        xlim(0, 200)
        ylim(0, 200)
        grid()
        show()


if __name__ == "__main__":
    cls1 = []
    cls2 = []
    cls3 = []

    # 分布1
    mean1 = [-2, 2]
    cov1 = [[1.0, 0.0], [0.0, 1.0]]

    # 分布2
    mean2 = [0, 0]
    cov2 = [[1.0, 0.8], [0.8, 1.0]]

    # 分布3
    mean3 = [2, -2]
    cov3 = [[0.5, 0.3], [0.8, 0.4]]

    # 分布にしたがうデータ生成 test
    cls1.extend(np.random.multivariate_normal(mean1, cov1, 100))
    cls2.extend(np.random.multivariate_normal(mean2, cov2, 100))
    cls3.extend(np.random.multivariate_normal(mean3, cov3, 100))
    X = vstack((cls1, cls2, cls3))
    print X
    #Corners 
    data = pd.read_csv("corners_value.csv")
    X = data.values
    np.random.shuffle(X)
    k = 4
    print X
    #Iris
    data = pd.read_csv("iris_value.csv")
    X = data.values
    np.random.shuffle(X)
    k = 3
    #print X
    

    # データをクラスタリング
    codebook, destortion = scipy.cluster.vq.kmeans(X, k, iter=20, thresh=1e-05)
    print codebook, destortion

    # ベクトル量子化
    # 各データをセントロイドに分類する
    code, dist = scipy.cluster.vq.vq(X, codebook)
    #show_plot(code, X)

