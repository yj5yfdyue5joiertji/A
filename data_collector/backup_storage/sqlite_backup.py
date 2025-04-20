# Faz cópia dos dados em SQLite (simples/local)
import sqlite3

def save_to_sqlite(candle, db_name='backup.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Cria tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candles (
            timestamp DATETIME,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL
        )
    ''')
    
    # Insere dados
    cursor.execute('''
        INSERT INTO candles VALUES (?, ?, ?, ?, ?, ?)
    ''', (candle['timestamp'], candle['open'], candle['high'], 
          candle['low'], candle['close'], candle['volume']))
    
    conn.commit()
    conn.close()

# Modo de usar:
candle = {
    'timestamp': "2025-03-10 01:00:00",
    'open': 81292.01,
    'high': 81888.00,
    'low': 80802.59,
    'close': 81766.01,
    'volume': 1700.61474
}
save_to_sqlite(candle)