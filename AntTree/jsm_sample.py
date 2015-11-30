# -*- coding:utf-8 -*-
#株価取得 jsm sample
#株価を取得しcsvで保存する

import jsm
import datetime

#csvに保存
q = jsm.QuotesCsv()
#クラスに保存の場合
#q= jsm.Quotes()

start_date = datetime.date(2015,4,1)
end_date = datetime.date(2015,4,30)

#株価を取得しcsvに保存
#q.save_historical_prices("NTTData_April.csv", 9613, jsm.DAILY, start_date, end_date)
#クラスに保存の場合
#q.get_historical_prices(9613, jsm.DAILY, start_date, end_date)

#調整後終値からリターンインデックスを求める
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv("NTTData_April.csv", index_col=0,
                 names=['open','high','low','close','volume','_adj_close'],
                 parse_dates=True)
print df

dates = pd.date_range(start_date, end_date)
price = df['_adj_close']
price = price.reindex(dates).dropna()
#タイムスタンプでソート的な dropna()->NaN(Not a Number)を除外
returns = price.pct_change()
ret_index = (1 + returns).cumprod()
ret_index[0] = 1
print '='*30
print 'NTT Data return index : 2015-04-01 -- 2015-05-01 '
print ret_index 
