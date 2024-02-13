-- Lists all records in 'second_table' with a score >= 10 in MySQL
-- Records ordered by desc score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
