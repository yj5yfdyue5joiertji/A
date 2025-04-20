from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDBStorage:
    def __init__(self, token, org, bucket, url="http://localhost:8086"):
        self.client = InfluxDBClient(url=url, token=token)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.org = org
        self.bucket = bucket
    
    def save_candle(self, symbol, candle):
        point = Point("candles")\
            .tag("symbol", symbol)\
            .field("open", float(candle['open']))\
            .field("high", float(candle['high']))\
            .field("low", float(candle['low']))\
            .field("close", float(candle['close']))\
            .field("volume", float(candle['volume']))\
            .time(candle['timestamp'])
        
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)

# Uso (configure seu token e org):
# storage = InfluxDBStorage(token="seu_token", org="sua_org", bucket="cripto")
# storage.save_candle("BTC/USDT", candle)