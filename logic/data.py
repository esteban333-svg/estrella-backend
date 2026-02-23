
import ccxt


def obtener_precio(symbol="BTC/USDT"):
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker(symbol)
    return ticker["last"]

def velas_binance(par="BTC/USDT", timeframe="1h", limite=200):
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(par, timeframe=timeframe, limit=limite)
    # ohlcv: [timestamp, open, high, low, close, volume]
    return ohlcv