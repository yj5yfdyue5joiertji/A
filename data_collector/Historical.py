import ccxt
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")  # Adiciona o diretório pai ao sys.path
## Importa a biblioteca ccxt para coletar dados de exchanges
## Importa o pandas para manipulação de dados
import pandas as pd

def get_historical_data(exchange_name='binance', symbol='BTC/USDT', timeframe='1h', limit=1000):
    exchange = getattr(ccxt, exchange_name)()  # Conecta à exchange
    candles = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)  # Pega candles
    
    # Converte para DataFrame
    df = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Converte timestamp
    
    return df

# Teste
if __name__ == "__main__":
    btc_data = get_historical_data()
    print(btc_data.head())  # Mostra as primeiras 5 linhas