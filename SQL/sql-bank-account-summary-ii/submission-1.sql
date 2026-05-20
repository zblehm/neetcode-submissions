-- Write your query below
SELECT name, SUM(amount) as balance
FROM users
JOIN transactions ON users.account = transactions.account
GROUP BY users.account
HAVING SUM(amount) > 10000;