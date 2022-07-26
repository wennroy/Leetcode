# 笨方法
# Write your MySQL query statement below
SELECT DISTINCT l1.Num ConsecutiveNums FROM Logs l1
LEFT JOIN Logs l2
ON l1.Id = l2.Id - 1
LEFT JOIN Logs l3
ON l1.Id = l3.Id - 2
WHERE l1.Num = l2.Num AND l2.Num = l3.Num;
# 利用窗口函数的方法

SELECT DISTINCT Num FROM (
SELECT Num,COUNT(1) as SerialCount FROM
(SELECT Id,Num,
row_number() over(order by id) -
ROW_NUMBER() over(partition by Num order by Id) as SerialNumberSubGroup
FROM ContinueNumber) as Sub
GROUP BY Num,SerialNumberSubGroup HAVING COUNT(1) >= 3) as Result

# 作者：neilsons
# 链接：https://leetcode.cn/problems/consecutive-numbers/solution/sql-server-jie-fa-by-neilsons/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 自己按着写的版本
# 若把row_number() over(order by id)换成Id，会报超出BIGINT UNSIGNED的错？？
# Write your MySQL query statement below
SELECT DISTINCT t.Num ConsecutiveNums FROM (
    SELECT Id, Num, row_number() over(order by id) - ROW_NUMBER() over(partition by Num order by Id) AS SerialNumberSubGroup FROM Logs
) AS t
GROUP BY t.SerialNumberSubGroup, t.Num
HAVING count(*) >= 3;
