import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px

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

# show volatility
data['30-Day Volatility'].plot(figsize=(10,6), title="30-Day Rolling Volatility")
#save plots as an image
plt.savefig('stock_vol_plot.png')
plt.show()


# statistical analysis 
# find sharpe ratio (assuming risk free rate of zero)
sharpe_ratio = data['Daily Return'].mean() / data['Daily Return'].std()
print(f'Sharpe Ratio: {sharpe_ratio}')

# create interactive charts for better analysis
fig = px.line(data, x=data.index, y='Close', title='Interactive Stock Price')
fig.show()

# save data to csv file for future analysis
data.to_csv('stock_data_analysis.csv')

# things to add: 
# backtest strategy like buying
# when 50-day ma crosses above 200-day ma (which is the golden cross)
# and sell when it crosses below (which is the death cross)

# comparing multiple stocks and analyze them together
# Risk analysis using VaR
# analyzing news and investor sentiment to predict moves in price