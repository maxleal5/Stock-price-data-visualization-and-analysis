import yfinance as yf
import matplotlib.pyplot as plt

# choose a stock symbol 
stock = yf.Ticker('MSTR')
# choose timeframe
data = stock.history(period='5y')

# print(data.tail())

#check to find missing values
# print(data.isnull().sum())

# fill any missing values using the forward fill method
data = data.fillna(method='ffill')

# now to calculate metrics 

# calculate daily returns as percentage from (dayClose - dayBeforeClose)/dayBeforeClose
data['Daily Return'] = data['Close'].pct_change()

#calculating 50 and 200 day moving avgs 
# data['50']
print(data.tail())