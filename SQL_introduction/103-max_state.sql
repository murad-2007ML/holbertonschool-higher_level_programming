-- average temperature0
SELECT state, MAX(value) AS max_value FROM temperatures GROUP BY state ORDER BY state;
