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
data['50-Day MA']= data['Close'].rolling(window=50).mean()
data['200-Day MA']= data['Close'].rolling(window=200).mean()

# adding 30 day volatility
data['30-Day Volatility'] = data['Daily Return'].rolling(window=30).std() * (252**.05) # annualized vol
# print(data.tail())

# plotting price with moving avgs
plt.figure(figsize=(10,6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['50-Day MA'], label='50-Day Moving Average')
plt.plot(data['200-Day MA'], label='200-Day Moving Average')
plt.title('Stock Price and Moving Averages')
plt.legend()
plt.show()

# show daily returns
data['Daily Return'].plot(figsize=(10,6),title='Daily Returns')
plt.show()
