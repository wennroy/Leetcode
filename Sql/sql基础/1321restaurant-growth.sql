# Write your MySQL query statement below
with temp AS (
    SELECT customer_id, visited_on, dense_rank() over(order by visited_on ASC) as rank_num, amount FROM Customer
)
SELECT DISTINCT t1.visited_on, SUM(t2.amount) amount, ROUND(SUM(t2.amount)/7,2) average_amount FROM temp t1, temp t2
WHERE t1.rank_num >= 7 AND t1.rank_num >= t2.rank_num AND t1.rank_num - 7 < t2.rank_num
GROUP BY t1.visited_on, t1.customer_id
ORDER BY t1.visited_on;

# group by 的时候要同时group by customer_id, 没有的话，会导致计算了两遍
# 当你以为你的解法很美妙，点开题解，发现自己就是小儿科

SELECT visited_on,amount,average_amount
FROM (
    SELECT visited_on,
           SUM(amount) OVER (ORDER BY visited_on ROWS 6 PRECEDING) AS amount,
           ROUND(AVG(amount)OVER(ORDER BY visited_on ROWS 6 PRECEDING),2) AS average_amount
    FROM (
        SELECT visited_on,SUM(amount) AS amount
        FROM Customer
        GROUP BY visited_on
    ) TABLE_1
) TABLE_2
WHERE DATEDIFF(visited_on,(SELECT MIN(visited_on) FROM Customer)) >=6


# 作者：avvesome-galoisrpm
# 链接：https://leetcode.cn/problems/restaurant-growth/solution/1321-by-avvesome-galoisrpm-l3u3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

SELECT DISTINCT visited_on,
       sum_amount AS amount,
       ROUND(sum_amount/7, 2) AS average_amount
-- 以上是破解【绊子1】并计算平均值，少用一次窗口函数提高运行速度
FROM (
    SELECT visited_on,
       SUM(amount) OVER ( ORDER BY visited_on ROWS 6 PRECEDING ) AS sum_amount
    -- 以下是计算每天的金额总量，破解【绊子2】
    FROM (
        SELECT visited_on,
            SUM(amount) AS amount
        FROM Customer
        GROUP BY visited_on
         ) TT
     ) LL
-- 最后手动只要覆盖完整7天的数据，破解【绊子1】
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6

# 作者：i2439786585
# 链接：https://leetcode.cn/problems/restaurant-growth/solution/jiang-jie-bing-gai-jin-ping-lun-qu-da-la-34xv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。