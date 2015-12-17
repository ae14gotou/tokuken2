# -*- coding: utf-8 -*-
import datetime
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

companies = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス'}
            #↑printでの表示は工夫が必要(日本語の部分)... とりあえず使いたいのはkeyだけ

def graph_Move_Average(code, start_date, end_date, n):
    #csvファイルの読み込み(DataFrame型)
    #test(2015,2,23 -- 2015,4,3) ->30次元 data(2015,4,1 -- 2015,11,30) ->163次元
    #df = pd.read_csv("csvfiles/"+ str(code) +"_test.csv", index_col=0,
    df = pd.read_csv("csvfiles/"+ str(code) +"_data.csv", index_col=0,
                 names=['open','high','low','close','volume','_adj_close'],
                 parse_dates=True)
    #print df
    dates = pd.date_range(start_date, end_date)
    price = df['_adj_close']
    price = price.reindex(dates).dropna()
    #タイムスタンプでソート的な dropna()->NaN(Not a Number)を除外
    #print price, len(price)
    sma_n = pd.rolling_mean(price, window=n)
    sma_n10 = pd.rolling_mean(price, window=n+10)
    sma_n.plot(label='SMA_'+str(n))
    sma_n10.plot(label='SMA_'+str(n+10))
    plt.legend(loc="best")
    plt.title(str(code))
    plt.show()

    
def get_Move_Average(code, start_date, end_date, n):
    #csvファイルの読み込み(DataFrame型)
    #test(2015,2,23 -- 2015,4,3) ->30次元 data(2015,4,1 -- 2015,11,30) ->163次元
    #df = pd.read_csv("csvfiles/"+ str(code) +"_test.csv", index_col=0,
    df = pd.read_csv("csvfiles/"+ str(code) +"_data.csv", index_col=0,
                 names=['open','high','low','close','volume','_adj_close'],
                 parse_dates=True)
    #print df
    dates = pd.date_range(start_date, end_date)
    price = df['_adj_close']
    price = price.reindex(dates).dropna()
    #タイムスタンプでソート的な dropna()->NaN(Not a Number)を除外
    #print price, len(price)
    sma_n = pd.rolling_mean(price, window=n)
    #sma5 = pd.rolling_mean(price, window=5)
    sma_n = sma_n.dropna()
    return sma_n.values, sma_n.index      
    
def make_Move_Average_files(start_date, end_date, n):
    T1 = [] #リターンインデックス（値）用
    T2 = [] #銘柄コード用
    D1 = {} #ディクショナリ型,DataFrame型をつくるため
    t = []
    code = companies.keys()
    for i in code:
        s,t = get_Move_Average(i, start_date, end_date, n)
        T1.append(s)
        T2.append(i)
        D1[i] = s

    T1 = pd.DataFrame(T1)
    print 'T1:'
    print T1
    #T1.to_csv('MoveAve_'+str(n)+'_values.csv', index=False, header=True) #save csv
    T2 = pd.DataFrame(T2)
    print 'T2:'
    print T2
    #T2.to_csv('MoveAve_'+str(n)+'_codes.csv', index=False, header=True) #save csv

    #print t[n+1:], len(t[n+1:])
    #D = pd.DataFrame(D,index=t[n+1:])
    #print D
    #print D.columns
    #D.to_csv('MoveAve_all.csv') #save csv
    print t
    return t

#if __name__ == '__main__':
def main(s, e, n):
    s = datetime.date(2015,4,1)
    e = datetime.date(2015,6,29)
    t = make_Move_Average_files(s,e,10)
    #graph_Move_Average(2327,s,e,10)
    return t

   
