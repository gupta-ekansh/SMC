import time
import datetime
import pandas as pd
import sys
import pickle
# ticker = '^NSEI'
# period1 = int(time.mktime(datetime.datetime(2022 , 7 , 1 , 23 , 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2023 , 7 , 1 , 23 , 59).timetuple()))
# interval = '1d'
# res = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

# print(res)

# df = pd.read_csv(res)
# df.insert(0 , 'Name' , 'Nifty')
# df.to_csv('nifty.csv')
# print(df.to_string())
data = [1,2,3,4,5]
print(sys.getsizeof(data))
data = pickle.dumps(data)
print(sys.getsizeof(data))
