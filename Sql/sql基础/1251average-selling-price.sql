# Write your MySQL query statement below
# 一次查询找到所有结果

SELECT p.product_id, ROUND(SUM(u.units*p.price)/SUM(u.units),2) average_price FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id
WHERE u.purchase_date between start_date AND end_date
GROUP BY p.product_id;

# 标答

SELECT
    product_id,
    Round(SUM(sales) / SUM(units), 2) AS average_price
FROM (
    SELECT
        Prices.product_id AS product_id,
        Prices.price * UnitsSold.units AS sales,
        UnitsSold.units AS units
    FROM Prices
    JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id
    WHERE UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
) T
GROUP BY product_id

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/average-selling-price/solution/ping-jun-shou-jie-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。