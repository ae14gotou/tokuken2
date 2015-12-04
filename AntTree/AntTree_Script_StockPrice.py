
#---------------------------------------------------------------------
#AntTreeアルゴリズムを用いたクラスタリングシステム
#--STOCH -> 確率論的アルゴリズム
#--NO_THRESHOLDS -> 決定論的アルゴリズム
#--K-means法は比較用に作成
#--株価はyahoo! financeから2015年4/1～11/30までの営業日で取得
#---------------------------------------------------------------------

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
import Return_Index as r_index
#date 4/1～11/30まで
start_date = datetime.date(2015,4,1)
end_date = datetime.date(2015,9,1)
companies = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス'}
            #↑printでの表示は工夫が必要... とりあえず使いたいのはkeyだけ

print 'term : '+str(start_date)+' -- '+str(end_date)
dates = r_index.main(start_date, end_date)

#--- STOCH_StockPrice ---
Ant, X, count = st_sp.main()
label = cl_ant.ant_label(Ant)

tmp = []
label_max = max(label)
for i in range(label_max+1):
    tmp.append({})

c = 0
codes = companies.keys()
#グラフ描画の準備
for i in label:
    for j in range(label_max+1):
        if j == i:
            tmp[i][codes[c]] = X[c]
        else : pass
    c = c+1

print label
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i], index=dates)
    print df
    df.plot() #グラフ描画
    plt.title('STOCH: Cluster'+str(i))
    plt.show()

#--- NO_THRESHOLDS_StockPrice ---
Ant, X, count = nt_sp.main()
label = cl_ant.ant_label(Ant)

tmp = []
label_max = max(label)
for i in range(label_max+1):
    tmp.append({})

c = 0
codes = companies.keys()
#グラフ描画の準備
for i in label:
    for j in range(label_max+1):
        if j == i:
            tmp[i][codes[c]] = X[c]
        else : pass
    c = c+1

print label
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i], index=dates)
    print df
    df.plot() #グラフ描画
    plt.title('NO_THRESHOLDS: Cluster'+str(i))
    plt.show()

#--- K-means ---
k = 10 #クラスタ数 
label, X = kmeans.main('return_index_values.csv',k)

tmp = []
label_max = max(label)
for i in range(label_max+1):
    tmp.append({})

c = 0
codes = companies.keys()
#グラフ描画の準備
for i in label:
    for j in range(label_max+1):
        if j == i:
            tmp[i][codes[c]] = X[c]
        else : pass
    c = c+1

print label
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i], index=dates)
    print df
    df.plot() #グラフ描画
    plt.title('K-means: Cluster'+str(i))
    plt.show()
