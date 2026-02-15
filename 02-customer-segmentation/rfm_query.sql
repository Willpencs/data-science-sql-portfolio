-- Objetivo: Extrair métricas RFM (Recency, Frequency, Monetary)
-- Este código consolida dados de pedidos e pagamentos por usuário único.

WITH customer_orders AS (
    SELECT 
        c.customer_unique_id,
        o.order_id,
        o.order_purchase_timestamp,
        p.payment_value
    FROM 
        orders AS o
    JOIN 
        customers AS c ON o.customer_id = c.customer_id
    JOIN 
        payments AS p ON o.order_id = p.order_id
    WHERE 
        o.order_status = 'delivered'
)
SELECT 
    customer_unique_id,
    -- Recência: Diferença em dias entre a última compra do dataset e a última do cliente
    julianday((SELECT MAX(order_purchase_timestamp) FROM customer_orders)) - 
    julianday(MAX(order_purchase_timestamp)) AS recency,
    -- Frequência: Contagem de pedidos distintos
    COUNT(DISTINCT order_id) AS frequency,
    -- Valor Monetário: Soma total de pagamentos
    SUM(payment_value) AS monetary
FROM 
    customer_orders
GROUP BY 
    customer_unique_id;
