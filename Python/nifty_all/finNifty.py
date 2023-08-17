import time
import datetime
import pandas as pd

ticker = 'NIFTY_FIN_SERVICE.NS'
period1 = int(time.mktime(datetime.datetime(2022 , 7 , 1 , 23 , 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2023 , 7 , 1 , 23 , 59).timetuple()))
interval = '1d'
res = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

print(res)

df = pd.read_csv(res)
df.insert(0 , 'Name' , 'Fin Nifty')
df.rename(columns={0:'index'}, inplace = True)
df.to_csv('finNifty.csv')