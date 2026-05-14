-- Write your query below
SELECT ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM delivery), 2) AS immediate_percentage
FROM delivery
WHERE order_date = customer_pref_delivery_date;