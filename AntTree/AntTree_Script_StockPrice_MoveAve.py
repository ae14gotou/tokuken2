
#---------------------------------------------------------------------
#AntTreeアルゴリズムを用いた(株価データ)クラスタリングシステム
#--STOCH -> 確率論的アルゴリズム
#--NO_THRESHOLDS -> 決定論的アルゴリズム
#---- Memo -----------------------------------------------------------
#--K-means法は比較用に作成
#--株価はyahoo! financeから2015年4/1～11/30までの営業日で取得
#--12/8追記 4/1～9/15(100次元)でメモリエラー発生 -> クラスタリングできていない
#--4/1～9/1(90次元)はできる
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
import RSI as rsi
import Move_Average as m_ave
#date 4/1～11/30まで
start_date = datetime.date(2015,4,1)
end_date = datetime.date(2015,6,29)
companies = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス'}
            #↑printでの表示は工夫が必要... とりあえず使いたいのはkeyだけ

print 'term : '+str(start_date)+' -- '+str(end_date)
#start_dateからend_dateまでの期間のリターンインデックスを計算，csvファイルで保存
#戻り値は営業日のdatetimeオブジェクト
dates = r_index.main(start_date, end_date)
fname1 = 'return_index_values.csv'
fname2 = 'return_index_codes.csv'

#start_dateからend_dateまでのRSIを計算，csvファイルで保存
#戻り値はdatetimeオブジェクト
#n = 14 #14日間でのRSI
#dates = rsi.main(start_date, end_date, n)
#fname1 = 'RSI_values.csv'
#fname2 = 'RSI_codes.csv'

print 'dates : ', len(dates)

#--- STOCH_StockPrice ---
Ant, X, count = st_sp.main(0.99, 0.1, fname1, fname2) #引数1:alpha1, 引数2:alpha2
label = cl_ant.ant_label(Ant)

tmp = []
label_max = max(label) #クラスタ数
for i in range(label_max+1):
    tmp.append({})

c = 0 #counter
codes = companies.keys()
#グラフ描画の準備
for i in label:
    for j in range(label_max+1):
        if j == i:
            tmp[i][codes[c]] = X[c]
        else : pass
    c = c+1
    
print ""
print "STOCH : ",label

#クラスタごとにグラフを表示
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i], index=dates)
    print ""
    print df
    df.plot() #グラフ描画
    plt.title('STOCH: Cluster'+str(i))
    plt.show()

#--- NO_THRESHOLDS_StockPrice ---
Ant, X, count = nt_sp.main(fname1, fname2)
label = cl_ant.ant_label(Ant)

tmp = []
label_max = max(label) #クラスタ数
for i in range(label_max+1):
    tmp.append({})

c = 0 #counter
codes = companies.keys()
#グラフ描画の準備
for i in label:
    for j in range(label_max+1):
        if j == i:
            tmp[i][codes[c]] = X[c]
        else : pass
    c = c+1

print ""
print "NO_THRESHOLDS: ",label
#クラスタごとにグラフを表示
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i], index=dates)
    print ""
    print df
    df.plot() #グラフ描画
    plt.title('NO_THRESHOLDS: Cluster'+str(i))
    plt.show()

#--- K-means ---
k = 7 #クラスタ数 
label, X = kmeans.main(fname1, k)

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

print ""
print "K-means: ",label
#クラスタごとにグラフを表示
for i in range(label_max+1):
    df = pd.DataFrame(tmp[i], index=dates)
    print ""
    print df
    df.plot() #グラフ描画
    plt.title('K-means: Cluster'+str(i))
    plt.show()
