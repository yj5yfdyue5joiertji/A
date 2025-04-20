import asyncio
import websockets
import json

async def binance_websocket(symbol='btcusdt'):
    uri = f"wss://stream.binance.com:9443/ws/{symbol}@kline_1h"
    
    async with websockets.connect(uri) as websocket:
        while True:
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
            
            # Aqui você vai salvar no banco de dados

# Para rodar:
asyncio.get_event_loop().run_until_complete(binance_websocket())