import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt
import talib as ta

tsla_df = yf.download('TSLA',
                      start='2019-01-01',
                      end='2020-12-31',
                      progress=False)
print(tsla_df.head())
print(len(tsla_df))

tsla_df['Close'].plot(title="TSLA's stock price")
tsla_df['MA'] = ta.SMA(tsla_df['Close'],20)
tsla_df['MA'].plot()

tsla_df['up_band'], tsla_df['mid_band'], tsla_df['low_band'] = ta.BBANDS(tsla_df['Close'], timeperiod =20)
for col in  ['Close','up_band','mid_band','low_band']:
    tsla_df[col].plot()

plt.show()
