# -*- coding:utf-8 -*-

import datetime
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

start_date = datetime.date(2015,2,23)
end_date = datetime.date(2015,4,3)
companies = {9682:'DTS', 9742:'アイネス', 9613:'NTTデータ', 2327:'新日鉄住金ソリューションズ',
             9640:'セゾン情報システムズ', 3626:'ITホールディングス', 2317:'システナ',
             4684:'オービック', 9739:'NSW', 4726:'ソフトバンク・テクノロジー', 4307:'野村総合研究所',
             9719:'SCSK', 4793:'富士通ビー・エス・シー', 4812:'電通国際情報サービス', 8056:'日本ユニシス'}
            #↑printでの表示は工夫が必要... とりあえず使いたいのはkeyだけ


def get_returnindex(code):
    #csvファイルの読み込み(DataFrame型)
    df = pd.read_csv("csvfiles/"+ str(code) +"_test.csv", index_col=0,
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
    print '='*30
    print str(code) + ' return index : '+str(start_date)+' -- '+str(end_date)
    print ret_index

    return ret_index.values.tolist()

def make_returnindex_files():
    T1 = []
    T2 = []
    code = companies.keys()
    for i in code:
        T1.append(get_returnindex(i))
        T2.append(i)

    T1 = pd.DataFrame(T1)
    T1.to_csv('return_index_values.csv', index=False, header=False)
    T2 = pd.DataFrame(T2)
    T2.to_csv('return_index_codes.csv', index=False, header=False)
    
if __name__ == '__main__' :
    make_returnindex_files()
