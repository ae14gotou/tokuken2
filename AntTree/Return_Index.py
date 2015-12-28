# -*- coding:utf-8 -*-

import datetime
import pandas as pd
from pandas import Series, DataFrame

#s_date = datetime.date(2015,4,1)
#e_date = datetime.date(2015,6,30)
'''
companies = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス',
             3765:'ガンホー・オンライン・エンターテイメント', 4689:'ヤフー', 4716:'日本オラクル',
             4739:'伊藤忠テクノソリューションズ', 4825:'ウェザーニュース', 7844:'マーベラス', 9432:'日本電信電話',
             9433:'KDDI', 9437:'NTTドコモ', 9697:'カプコン', 9766:'コナミ', 9984:'ソフトバンクグループ',
             9749:'富士ソフト', 3632:'グリー', 3656:'KLab'}
            #↑printでの表示は工夫が必要(日本語の部分)... とりあえず使いたいのはkeyだけ
'''

def get_returnindex(code, start_date, end_date):
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
    #調整後終値からリターンインデックスを求める
    returns = price.pct_change()
    ret_index = (1 + returns).cumprod()
    ret_index[0] = 1
    #print '='*30
    #print str(code) + ' return index : '+str(start_date)+' -- '+str(end_date)
    #print ret_index.index

    return ret_index.values.tolist(), ret_index.index

def make_returnindex_files(s_date, e_date, companies):
    T1 = [] #リターンインデックス（値）用
    T2 = [] #銘柄コード用
    D = {} #ディクショナリ型,DataFrame型をつくるため
    t = []
    code = companies.keys()
    for i in code:
        s,t = get_returnindex(i, s_date, e_date)
        T1.append(s)
        T2.append(i)
        D[i] = s

    T1 = pd.DataFrame(T1)
    T1.to_csv('return_index_values.csv', index=False, header=True) #save csv
    T2 = pd.DataFrame(T2)
    T2.to_csv('return_index_codes.csv', index=False, header=True) #save csv
    #print t, len(t)
    #D = pd.DataFrame(D,index=t)
    #print D
    #print D.columns
    #D.to_csv('return_index_all.csv') #save csv

    return t
    
#if __name__ == '__main__' :
def main(s_date, e_date, company_dict):
    t_index = make_returnindex_files(s_date, e_date, company_dict)
    return t_index
    
