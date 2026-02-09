import os
import pandas as pd
import sqlite3

# 1. Localizando os arquivos automaticamente no sistema Linux do Kaggle
paths = {}
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        if filename.endswith('.csv'):
            paths[filename] = os.path.join(dirname, filename)

# 2. Carregando os dados crus para o ambiente de Engenharia
if 'olist_orders_dataset.csv' in paths:
    orders = pd.read_csv(paths['olist_orders_dataset.csv'])
    payments = pd.read_csv(paths['olist_order_payments_dataset.csv'])
    
    # 3. Criando o banco de dados SQL na memória (SQLite)
    conn = sqlite3.connect(':memory:')
    orders.to_sql('orders', conn, index=False)
    payments.to_sql('payments', conn, index=False)
    
    print(f"✅ Sucesso! {len(paths)} arquivos CSV prontos para uso.")
    print(f"📊 Total de pedidos carregados: {len(orders)}")
else:
    print("❌ Erro: Os arquivos não foram encontrados no Input.")
