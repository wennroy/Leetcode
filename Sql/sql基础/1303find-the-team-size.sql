# 相关子查询
# Write your MySQL query statement below
SELECT employee_id, t.team_size FROM Employee e1
LEFT JOIN (
    SELECT team_id, count(*) team_size FROM Employee
    GROUP BY team_id
) AS t
ON e1.team_id = t.team_id;


# Window Function
SELECT
    employee_id,
    COUNT(employee_id) OVER(PARTITION BY team_id) AS team_size
FROM Employee
ORDER BY employee_id;


# 自连结
# Self Join
SELECT e1.employee_id, COUNT(*) AS team_size
FROM Employee e1 JOIN Employee e2 USING (team_id)
GROUP BY e1.employee_id
ORDER BY e1.employee_id;

# 作者：Markov015
# 链接：https://leetcode.cn/problems/find-the-team-size/solution/san-chong-fang-fa-self-join-correlated-subquerry-w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。