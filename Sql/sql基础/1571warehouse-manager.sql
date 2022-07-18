# JOIN 和 GROUPBY SUM 由于题目设定，内连接或者外连接应该都是符合条件的
# Write your MySQL query statement below
SELECT name warehouse_name, ROUND(SUM(p.Width*p.Length*p.Height*w.units)) volume FROM Warehouse w
LEFT JOIN Products p
ON p.product_id = w.product_id
GROUP BY name;
