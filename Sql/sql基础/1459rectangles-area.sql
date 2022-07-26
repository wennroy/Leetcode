# Write your MySQL query statement below

SELECT t1.id P1, t2.id P2, abs(t1.x_value-t2.x_value)*abs(t1.y_value-t2.y_value) AS AREA FROM Points t1
CROSS JOIN Points t2
ON t1.id < t2.id
WHERE t1.x_value != t2.x_value AND t1.y_value != t2.y_value
ORDER BY AREA DESC, P1, P2;