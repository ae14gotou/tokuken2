# -*- coding:utf-8 -*-

import datetime
import pandas as pd
from pandas import Series,DataFrame

companies = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス'}
            #↑printでの表示は工夫が必要(日本語の部分)... とりあえず使いたいのはkeyだけ

def get_RSI_first(code, start_date, end_date, price):
    #最初のRSIをもとめる
    #tmp = price[:n]
    up_sum = 0
    down_sum = 0
    p = price[0]
    for i in price[1:]:
        diff = i - p
        #print diff
        if diff > 0: up_sum = up_sum + diff
        else : down_sum = down_sum + diff*(-1) #正にするため
        p = i

    #print up_sum, down_sum, len(price)-1
    A = round(up_sum/(len(price)-1), 3)
    B = round(down_sum/(len(price)-1), 3) 
    #print A, B

    RSI_first = round(A/(A+B)*100, 2)
    print RSI_first

    return A, B, RSI_first

def get_RSI(code, start_date, end_date,n):
    #csvファイルの読み込み(DataFrame型)
    #test(2015,2,23 -- 2015,4,3) ->30次元 data(2015,4,1 -- 2015,11,30) ->163次元
    #df = pd.read_csv("csvfiles/"+ str(code) +"_test.csv", index_col=0,
    df = pd.read_csv("csvfiles/"+ str(code) +"_data.csv", index_col=0,
                 names=['open','high','low','close','volume','_adj_close'],
                 parse_dates=True)
    print df
    dates = pd.date_range(start_date, end_date)
    price = df['_adj_close']
    price = price.reindex(dates).dropna()
    #タイムスタンプでソート的な dropna()->NaN(Not a Number)を除外
    print price[:n+1]
    r = []
    A, B, RSI_first = get_RSI_first(code,s,e,price[:n+1])
    r.append(RSI_first)
    p = price[n+1]
    
    for i in price[n+2:]:
        diff = i - p
        p_a = round(A*(n-1), 3)
        p_b = round(B*(n-1), 3)
        if diff > 0 : A = round((p_a+diff)/n, 3)
        else : B = round((p_b+(-1)*diff)/n, 3)
        print A,B
        r.append(round(A/(A+B)*100, 2))
        p = i
            
    print r
    print price.index
    return r,price.index
    
def make_RSI_files(start_date, end_date, n):
    T1 = [] #リターンインデックス（値）用
    T2 = [] #銘柄コード用
    D = {} #ディクショナリ型,DataFrame型をつくるため
    t = []
    code = companies.keys()
    for i in code:
        s,t = get_RSI(i, start_date, end_date, n)
        T1.append(s)
        T2.append(i)
        D[i] = s

    T1 = pd.DataFrame(T1)
    print T1
    #T1.to_csv('RSI_values.csv', index=False, header=True) #save csv
    T2 = pd.DataFrame(T2)
    print T2
    #T2.to_csv('RSI_codes.csv', index=False, header=True) #save csv
    print t[n+1:], len(t[n+1:])
    D = pd.DataFrame(D,index=t[n+1:])
    print D
    #print D.columns
    #D.to_csv('RSI_all.csv') #save csv

    return t    

    

if __name__ == '__main__':
    s = datetime.date(2015,4,1)
    e = datetime.date(2015,4,30)
    t = make_RSI_files(s,e,14)

    
    
    
    
