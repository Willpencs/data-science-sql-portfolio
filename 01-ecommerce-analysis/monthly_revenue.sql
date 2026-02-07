-- Goal: Calculate Total Revenue per Month to track business growth
-- Dataset: Brazilian E-Commerce Public Dataset (Olist)

SELECT 
    -- Truncates the timestamp to the first day of the month for easy grouping
    DATE_TRUNC('month', order_purchase_timestamp) AS month, 
    
    -- Sums the payment values to get total monthly revenue
    SUM(payment_value) AS total_revenue,                  
    
    -- Counts unique orders to understand volume
    COUNT(DISTINCT o.order_id) AS total_orders             
FROM 
    `ecommerce_data.payments` AS p
JOIN 
    `ecommerce_data.orders` AS o ON p.order_id = o.order_id
WHERE 
    -- Business Rule: We only care about orders that were actually delivered
    o.order_status = 'delivered'                           
GROUP BY 
    1
ORDER BY 
    1 DESC;
