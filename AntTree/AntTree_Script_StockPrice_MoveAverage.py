﻿
#---------------------------------------------------------------------
#AntTreeアルゴリズムを用いた(株価データ)クラスタリングシステム
#--移動平均を使用するパターンの実行スクリプト
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
import Move_Average as m_ave
#date 4/1～11/30まで
start_date = datetime.date(2015,4,1)
end_date = datetime.date(2015,6,29)
#企業コードと企業名
companies_test = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス'}

companies_it = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス',
             3765:'ガンホー・オンライン・エンターテイメント', 4689:'ヤフー', 4716:'日本オラクル',
             4739:'伊藤忠テクノソリューションズ', 4825:'ウェザーニュース', 7844:'マーベラス', 9432:'日本電信電話',
             9433:'KDDI', 9437:'NTTドコモ', 9697:'カプコン', 9766:'コナミ', 9984:'ソフトバンクグループ',
             9749:'富士ソフト', 3632:'グリー', 3656:'KLab'} #情報通信系

companies_food = {2001:'日本製粉', 2002:'日清製粉グループ本社', 2003:'日東富士製粉', 2109:'三井製糖', 2201:'森永製菓',
             2206:'江崎グリコ', 2211:'不二家', 2212:'山崎製パン', 2217:'モロゾフ', 2220:'亀田製菓', 2229:'カルビー',
             2264:'森永乳業', 2267:'ヤクルト本社', 2270:'雪印メグミルク', 2281:'プリマハム', 2282:'日本ハム',
             2284:'伊藤ハム', 2288:'丸大食品', 2501:'サッポロホールディングス', 2502:'アサヒホールディングス', 2503:'キリンホールディングス',
             2579:'コカ・コーラウエスト', 2593:'伊藤園'} #食料品

companies_retail = {2651:'ローソン', 2681:'ゲオホールディングス', 2730:'エディオン', 3048:'ビックカメラ', 3197:'すかいらーく',
             3382:'セブン＆アイホールディングス', 7550:'ゼンショーホールディングス', 7581:'サイゼリヤ', 7630:'壱番屋',
             8028:'ファミリーマート', 8175:'ベスト電器', 8179:'ロイヤルホールディングス', 8200:'リンガーハット',
             9831:'ヤマダ電器'} #小売

companies_device = {4902:'コニカミノルタ', 6448:'ブラザー工業', 6501:'日立製作所', 6502:'東芝', 6503:'三菱電機',
             6506:'安川電機', 6516:'三洋電機', 6645:'オムロン', 6701:'NEC', 6702:'富士通', 6703:'OKI',
             6724:'セイコーエプソン', 6752:'パナソニック', 6753:'シャープ', 6758:'ソニー', 6762:'TDK',
             6981:'村田製作所', 7751:'キャノン', 7752:'リコー', 8035:'東京エレクトロン'} #電気機器

companies_service = {2193:'クックパッド', 2371:'カカクコム', 2379:'ディップ', 2433:'博報堂DIYホールディングス',
             2432:'ディー・エヌ・エー', 4324:'電通', 4751:'サイバーエージェント', 4755:'楽天'} #サービス

    #↑printでの表示は工夫が必要... とりあえず使いたいのはkeyだけ

companies = companies_device #クラスタリングする業種

print 'term : '+str(start_date)+' -- '+str(end_date)
#start_dateからend_dateまでの移動平均を計算，csvファイルで保存
#戻り値はdatetimeオブジェクト
n = 10 #10日間での移動平均
dates = m_ave.main(start_date, end_date, n, companies)
fname1 = 'MoveAve_'+str(n)+'_values.csv'
fname2 = 'MoveAve_'+str(n)+'_codes.csv'

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
print ""
print "STOCH : ",label
#会社コードとラベルの表示
for i in range(len(label)):
    print label[i], codes[i]
#移動平均のグラフを描画
for i in codes:
    m_ave.graph_Move_Average(i, start_date, end_date, n)

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
