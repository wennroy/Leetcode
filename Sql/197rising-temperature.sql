# Write your MySQL query statement below
SELECT w1.id id FROM Weather w1
LEFT JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
# DATEDIFF的用法 w1是w2的第二天。
