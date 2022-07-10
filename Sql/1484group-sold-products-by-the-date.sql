# 对于CONCAT 语句的练习
# 前置表的创建
USE leetcode;
DROP TABLE IF EXISTS activities;
CREATE TABLE IF NOT EXISTS activities (
    sell_date date,
    product varchar(255)
);

INSERT INTO activities
VALUES
    ('2020-05-30', 'Headphone'),
    ('2020-06-01', 'Pencil'),
    ('2020-06-02', 'Mask'),
    ('2020-05-30', 'Basketball'),
    ('2020-06-01', 'Bible'),
    ('2020-06-02', 'Mask'),
    ('2020-05-30', 'T-shirt');

SELECT * FROM activities;

# CONCAT 总结

SELECT a1.sell_date, CONCAT(a1.product, a2.product) products FROM activities a1, activities a2
WHERE a1.sell_date = a2.sell_date;

# CONCAT_WS

SELECT a1.sell_date, CONCAT_WS(
    ',',a1.product, a2.product
           ) products FROM activities a1, activities a2
WHERE a1.sell_date = a2.sell_date;

# 本题标答使用：GROUP_CONCAT

SELECT
    sell_date,
    COUNT(DISTINCT product) num_sold,
    GROUP_CONCAT(DISTINCT product) products
FROM
    activities
GROUP BY sell_date
ORDER BY sell_date;

# 作者：Jam007
# 链接：https://leetcode.cn/problems/group-sold-products-by-the-date/solution/by-jam007-hhi4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。