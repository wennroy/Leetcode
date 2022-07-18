# 与1699属于一样的题型， 解决方法就是先subsselect再select。其实也能写到一起，但有点长。
# Write your MySQL query statement below
SELECT sale_date, SUM(apples-oranges) diff FROM
(
    SELECT sale_date, IF(fruit = 'apples', sold_num, 0) apples, IF(fruit = 'oranges', sold_num, 0) oranges
    FROM Sales
) AS t
GROUP BY sale_date;

# case when 写法 记得加END
# Write your MySQL query statement below
SELECT sale_date,
    SUM(CASE WHEN fruit='apples' THEN sold_num ELSE -sold_num END) AS diff
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

# 作者：Jam007
# 链接：https://leetcode.cn/problems/apples-oranges/solution/by-jam007-lkl1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。