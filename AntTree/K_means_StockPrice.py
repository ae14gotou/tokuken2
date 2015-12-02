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


#if __name__ == "__main__":
def main(fname,k):
    #data file
    data = pd.read_csv(fname)
    X = data.values
    #np.random.shuffle(X)

    # データをクラスタリング
    codebook, destortion = scipy.cluster.vq.kmeans(X, k, iter=20, thresh=1e-05)
    #print codebook, destortion

    # ベクトル量子化
    # 各データをセントロイドに分類する
    code, dist = scipy.cluster.vq.vq(X, codebook)
    return code, X
    #show_plot(code, X)

