-- listing number of scores with same values
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC; 
