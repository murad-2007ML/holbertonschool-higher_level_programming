-- listing number of scores with same values
SELECT score, name FROM second_table GROUP BY score ORDER BY count DESC; 
