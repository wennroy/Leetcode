# Write your MySQL query statement below
# 简单的自连接

SELECT e1.reports_to employee_id, e2.name, COUNT(*) reports_count, ROUND(AVG(e1.age),0) average_age FROM Employees e1
INNER JOIN Employees e2
ON e1.reports_to = e2.employee_id
GROUP BY e1.reports_to
ORDER BY e1.reports_to;
