import talib
import yfinance as yf

# yfinance: https://pypi.org/project/yfinance/

# If you have an error "JSON decode" https://bit.ly/3xWD49Q

# Fetching data for multiple tickers
data = yf.download("BTC-USD", start="2014-09-17", end="2021-07-20")

### TA-LIB - Pattern Recognition Functions: https://bit.ly/3wMO3Bj

# CDLMORNINGSTAR - Morning Star
morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

# CDLENGULFING - Engulfing Pattern
engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])


data['Morning Star'] = morning_star
data['Engulfing'] = engulfing


morning_star = data[data['Morning Star'] != 0]
engulfing_days = data[data['Engulfing'] != 0]

print(morning_star)
print(engulfing_days)
print(data)

# print(engulfing_days)