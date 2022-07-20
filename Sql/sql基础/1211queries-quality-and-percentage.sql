# Write your MySQL query statement below
SELECT query_name, ROUND(AVG(rating/position),2) quality, ROUND(SUM(IF(rating<3,1,0))/SUM(1)*100,2) poor_query_percentage
FROM Queries q
GROUP BY query_name;

# SUM(1) = COUNT(*)