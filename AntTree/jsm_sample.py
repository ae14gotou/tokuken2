#株価取得 jsm sample
#株価を取得しcsvで保存する

import jsm
import datetime

#csvに保存
q = jsm.QuotesCsv()
#クラスに保存の場合
#q= jsm.Quotes()

start_date = datetime.date(2015,4,1)
end_date = datetime.date(2015,5,1)

#株価を取得しcsvに保存
q.save_historical_prices("NTTData.csv", 9613, jsm.DAILY, start_date, end_date)
#クラスに保存の場合
#q.get_historical_prices(9613, jsm.DAILY, start_date, end_date)
