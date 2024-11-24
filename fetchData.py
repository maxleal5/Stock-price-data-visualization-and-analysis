import yfinance as yf

# choose a stock symbol 
stock = yf.Ticker('MSTR')
# choose timeframe
data = stock.history(period='5y')

# print(data.tail())

#check to find missing values
# print(data.isnull().sum())

# fill any missing values using the forward fill method
data = data.fillna(method='ffill')
