# Verifica se os candles não estão corrompidos
def is_valid_candle(candle):
    if (candle['high'] < candle['low'] or 
        candle['open'] > candle['high'] or 
        candle['volume'] < 0):
        return False
    return True

# Modo de usar:
candle = {'open': 500, 'high': 520, 'low': 490, 'close': 515, 'volume': 1000}
if is_valid_candle(candle):
    print("Candle OK!")
else:
    print("Candle ZOADO! 🐙")