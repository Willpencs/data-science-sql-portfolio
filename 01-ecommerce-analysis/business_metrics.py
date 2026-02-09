# Trecho para o seu arquivo de métricas no portfólio
import pandas as pd

# Cálculo do Ticket Médio Mensal
query_ticket = """
SELECT 
    strftime('%Y-%m', order_purchase_timestamp) AS mes,
    ROUND(AVG(payment_value), 2) AS ticket_medio
FROM 
    payments AS p
JOIN 
    orders AS o ON p.order_id = o.order_id
WHERE 
    order_status = 'delivered'
GROUP BY 1
ORDER BY 1 ASC
"""

df_ticket = pd.read_sql_query(query_ticket, conn)
print("--- Ticket Médio Mensal (Últimos meses) ---")
print(df_ticket.tail())
