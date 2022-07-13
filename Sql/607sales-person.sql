# Write your MySQL query statement below
SELECT DISTINCT s.name FROM SalesPerson s
LEFT JOIN Orders o
ON s.sales_id = o.sales_id
LEFT JOIN Company c
ON c.com_id = o.com_id
WHERE s.sales_id NOT IN (
    SELECT o.sales_id FROM Orders o, Company c
    WHERE c.name = 'RED' AND o.com_id = c.com_id
);


# 官方标答
#
SELECT
    s.name
FROM
    salesperson s
WHERE
    s.sales_id NOT IN (SELECT
            o.sales_id
        FROM
            orders o
                LEFT JOIN
            company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED')
;

# 作者：LeetCode
# 链接：https://leetcode.cn/problems/sales-person/solution/xiao-shou-yuan-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。