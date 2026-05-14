-- Write your query below
SELECT customer_number
FROM orders
GROUP By customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;