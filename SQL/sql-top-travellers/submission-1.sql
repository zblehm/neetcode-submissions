-- Write your query below

-- CREATE TABLE distance_or_zero AS
WITH distance_or_zero AS (
    SELECT name,
        CASE
            WHEN distance IS NULL THEN 0 
            ELSE distance
        END as distance
    FROM users LEFT JOIN rides ON users.id = rides.user_id
)

SELECT name, SUM(distance) AS travelled_distance
FROM distance_or_zero
GROUP BY name
ORDER BY travelled_distance DESC, name ASC;