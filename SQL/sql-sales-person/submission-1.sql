-- Write your query below

SELECT sales_person.name
FROM sales_person
WHERE sales_person.sales_id NOT IN (
    SELECT sales_person.sales_id
    FROM sales_person
    JOIN orders ON sales_person.sales_id = orders.sales_id
    JOIN company ON company.com_id = orders.com_id
    WHERE company.name = 'CRIMSON'
); 