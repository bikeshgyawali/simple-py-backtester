import yfinance as yf

def get_spy_data(ticker, start_date, end_date):
    spy_data = yf.download(ticker, start=start_date, end=end_date, multi_level_index=False)
    column_data = spy_data['Close'].dropna().tolist()
    return column_data