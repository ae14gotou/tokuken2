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
end_date = datetime.date(2015,11,30)

#2012/12/28 追加
codes_it = [3765, 4689, 4716, 4739, 4825, 7844, 9432, 9433,
         9437, 9697, 9766, 9984, 9749, 3632, 3656] #追加分
codes_food = [2001, 2002, 2003, 2109, 2201, 2206, 2211, 2212,
              2217, 2220, 2229, 2264, 2267, 2270, 2281, 2282,
              2284, 2288, 2501, 2502, 2503, 2579, 2593] #追加分
codes_retail = [2651, 2681, 2730, 3048, 3197, 3382, 7550, 7581,
                7630, 8028, 8175, 8179, 8200, 9831] #追加分
codes_electric = [4902, 6448, 6501, 6502, 6503, 6506, 6516, 6645,
                  6701, 6702, 6703, 6724, 6752, 6753, 6758, 6762,
                  6981, 7751, 7752, 8035] #追加分
codes_service = [2193, 2371, 2379, 2432, 2433, 4324, 4751, 4755] #追加分

for i in codes_service :
#株価を取得しcsvに保存
    q.save_historical_prices(str(i)+"_data.csv", i, jsm.DAILY, start_date, end_date)

#クラスに保存の場合
#q.get_historical_prices(9613, jsm.DAILY, start_date, end_date)

