# Sistema de backup caso Binance falhe
import ccxt

def get_exchange():
    exchanges = [
        'binance',   # Tenta primeiro
        'bybit',     # Segunda opção
        'okx'        # Terceira opção
    ]
    
    for exchange_name in exchanges:
        try:
            exchange = getattr(ccxt, exchange_name)()
            exchange.fetch_ohlcv('BTC/USDT', '1h', limit=1)  # Testa se funciona
            return exchange
        except:
            continue
    
    raise Exception("Todas exchanges falharam! 🚨")

# Modo de usar:
exchange = get_exchange()
print(f"Conectado à: {exchange.name}")