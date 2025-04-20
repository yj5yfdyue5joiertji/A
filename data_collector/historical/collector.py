import ccxt
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")  # Adiciona o diretório pai ao sys.path
## Importa a biblioteca ccxt para coletar dados de exchanges
## Importa o pandas para manipulação de dados
import pandas as pd

def get_historical_data(exchange_name='binance', symbol='BTC/USDT', timeframe='1h', limit=1000):
    for _ in range(3):  # Tenta 3 vezes se falhar
        try:
            exchange = getattr(ccxt, exchange_name)()
            candles = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            # ... (o resto do seu código atual)
                # Converte para DataFrame
            df = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Converte timestamp
            return df
        except Exception as e:
            print(f"Erro: {e}. Tentando novamente...")
            time.sleep(5)
    raise Exception("Não conseguiu pegar dados históricos após 3 tentativas")

# Teste
if __name__ == "__main__":
    btc_data = get_historical_data()
    print(btc_data.head())  # Mostra as primeiras 5 linhas