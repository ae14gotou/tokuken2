# -*- coding:utf-8 -*-

import datetime
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
#自作モジュールのインポート
import STOCH_StockPrice as st_sp
import NO_THRESHOLDS_StockPrice as nt_sp
import K_means_StockPrice as kmeans
import cluster_Ant as cl_ant

start_date = datetime.date(2015,2,23)
end_date = datetime.date(2015,4,3)
companies = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス'}
            #↑printでの表示は工夫が必要... とりあえず使いたいのはkeyだけ

print 'term : '+str(start_date)+' -- '+str(end_date)
t = pd.read_csv('csvfiles/return_index_all.csv')
t = t.set_index('date', drop=True)
#print t
#print t.index
dates = t.index
#print dates

#--- STOCH_StockPrice ---
Ant, X, count = st_sp.main()
label = cl_ant.ant_label(Ant)

tmp = []
label_max = max(label)
for i in range(label_max+1):
    tmp.append({})

D = {}
c = 0
codes = companies.keys()
for i in label:
    if i == 0:
        tmp[i][codes[c]] = X[c]
    elif i == 1:
        tmp[i][codes[c]] = X[c]
    elif i == 2:
        tmp[i][codes[c]] = X[c]
    elif i == 3:
        tmp[i][codes[c]] = X[c]
    else : pass
    c = c+1

print label
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i],index=dates)
    print df
    df.plot()
    plt.show()

#--- NO_THRESHOLDS_StockPrice ---
Ant, X, count = nt_sp.main()
label = cl_ant.ant_label(Ant)

tmp = []
label_max = max(label)
for i in range(label_max+1):
    tmp.append({})

D = {}
c = 0
codes = companies.keys()
for i in label:
    if i == 0:
        tmp[i][codes[c]] = X[c]
    elif i == 1:
        tmp[i][codes[c]] = X[c]
    elif i == 2:
        tmp[i][codes[c]] = X[c]
    elif i == 3:
        tmp[i][codes[c]] = X[c]
    else : pass
    c = c+1

print label
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i],index=dates)
    print df
    df.plot()
    plt.show()

#--- K-means ---
k = 4 #クラスタ数
label, X = kmeans.main('csvfiles/return_index_values.csv',k)

tmp = []
label_max = max(label)
for i in range(label_max+1):
    tmp.append({})

D = {}
c = 0
codes = companies.keys()
for i in label:
    if i == 0:
        tmp[i][codes[c]] = X[c]
    elif i == 1:
        tmp[i][codes[c]] = X[c]
    elif i == 2:
        tmp[i][codes[c]] = X[c]
    elif i == 3:
        tmp[i][codes[c]] = X[c]
    else : pass
    c = c+1

print label
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i],index=dates)
    print df
    df.plot()
    plt.show()
