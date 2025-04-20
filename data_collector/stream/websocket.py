import asyncio
import websockets
import json
from data_collector.failover_system.exchange_fallback import get_exchange
from data_collector.data_validator.candle_checker import is_valid_candle
from data_collector.backup_storage.sqlite_backup import save_to_sqlite
from data_collector.storage.influxdb import InfluxDBStorage
import datetime

storage = InfluxDBStorage(token="ot5KhaV7EK4EB7KZYpmcHZFUqZtrMiUsTxaELEnj_xuJtTmev_fBNoyQCRE6OzFyhOTvie_FQeZuS6yqcxqqzg==", org="Trading bot", bucket="Trading Bot")

async def bybit_websocket(symbol='BTCUSDT'):
    uri = f"wss://stream.bybit.com/v5/public/linear/{symbol}@kline_1h"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            candle = {
                'timestamp': datetime.fromtimestamp(data['data']['start'] / 1000),
                'open': float(data['data']['open']),
                'high': float(data['data']['high']),
                'low': float(data['data']['low']),
                'close': float(data['data']['close']),
                'volume': float(data['data']['volume'])
            }
            storage.save_candle("BTC/USDT", candle)

async def binance_websocket(symbol='btcusdt'):
    uri = f"wss://stream.binance.com:9443/ws/{symbol}@kline_1h"
    
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                
                candle = {
                    'timestamp': data['k']['t'],
                    'open': data['k']['o'],
                    'high': data['k']['h'],
                    'low': data['k']['l'],
                    'close': data['k']['c'],
                    'volume': data['k']['v']
                }
                print("Novo candle:", candle)
                
                if is_valid_candle(candle):  # Só salva se for válido
                    storage.save_candle("BTC/USDT", candle)
                    save_to_sqlite(candle)  # Faz backup local
                else:
                    print("Candle inválido descartado!")
            except Exception as e:
                print("Conexão com Binance caiu! Trocando pra Bybit...")
                # Chama função para conectar a outra exchange
                await bybit_websocket(symbol)  # Você precisa criar essa função igual à Binance

# Para rodar:
asyncio.get_event_loop().run_until_complete(binance_websocket())