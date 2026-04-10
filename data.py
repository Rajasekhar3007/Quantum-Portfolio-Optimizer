import yfinance as yf

def get_data():
    stocks = ['AAPL', 'MSFT', 'GOOG', 'TSLA']
    
    data = yf.download(stocks, start="2022-01-01", end="2023-01-01")

    # Handle both cases safely
    if 'Adj Close' in data.columns:
        prices = data['Adj Close']
    else:
        prices = data['Close']  # fallback

    returns = prices.pct_change().dropna()
    
    return returns.mean(), returns.cov()
