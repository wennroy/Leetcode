# Write your MySQL query statement below
WITH temp AS (
    SELECT product_id, SUM(rest) rest_sum, SUM(paid) paid_sum, SUM(canceled) canceled_sum, SUM(refunded) refunded_sum FROM Invoice
    GROUP BY product_id
)
SELECT name, IFNULL(temp.rest_sum,0) rest, IFNULL(temp.paid_sum,0) paid,
IFNULL(temp.canceled_sum,0) canceled, IFNULL(temp.refunded_sum,0) refunded FROM Product
LEFT JOIN temp
ON Product.product_id = temp.product_id
ORDER BY name;
