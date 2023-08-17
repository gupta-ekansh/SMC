import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def buy_sell(data):
    signal = []
    position = False

    for i in range(len(data)):
        if data['5-day Avg'][i] > data['7-day Avg'][i]:
            if position == False:
                signal.append('Buy')
                position = True
            else:
                signal.append(np.nan)
        elif data['5-day Avg'][i] < data['High'][i]:
            if position == True:
                signal.append('Sell')
                position= False
            else:
                signal.append(np.nan)
        else:
            signal.append(np.nan)
    return signal


df1 = pd.read_csv('nifty.csv', index_col=[0])
df2 = pd.read_csv('bankNifty.csv', index_col=[0])
df3 = pd.read_csv('finNifty.csv', index_col=[0])


df1['5-day Avg'] = df1['High'].rolling(5).mean()
df1['7-day Avg'] = df1['High'].rolling(7).mean()
df1['Signal'] = buy_sell(df1)
df1.to_csv('nifty.csv')


df2['5-day Avg'] = df2['High'].rolling(5).mean()
df2['7-day Avg'] = df2['High'].rolling(7).mean()
df2['Signal'] = buy_sell(df2)
df2.to_csv('bankNifty.csv')



df3['5-day Avg'] = df3['High'].rolling(5).mean()
df3['7-day Avg'] = df3['High'].rolling(7).mean()
df3['Signal'] = buy_sell(df3)
df3.to_csv('finNifty.csv')
