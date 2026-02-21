import pandas as pd
import sqlite3
from datetime import datetime

def run_etl():
    print("Iniciando Pipeline ETL...")
    
    # 1. Extração (Extract) - Simulando consumo de API
    data = {
        'ticker': ['PETR4', 'VALE3', 'ITUB4', 'ABEV3'],
        'price': [35.50, 68.20, 32.10, 14.90],
        'volume': [1500, 2300, 1800, None] # Dado nulo para teste de limpeza
    }
    df = pd.DataFrame(data)
    
    # 2. Transformação (Transform)
    # Limpeza: Preenchendo valores nulos e adicionando timestamp
    df['volume'] = df['volume'].fillna(df['volume'].mean())
    df['extracted_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 3. Carga (Load)
    conn = sqlite3.connect('market_data.db')
    df.to_sql('stock_prices', conn, if_exists='replace', index=False)
    conn.close()
    
    print("Pipeline finalizado com sucesso e dados salvos no SQLite!")

if __name__ == "__main__":
    run_etl()
