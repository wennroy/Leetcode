# Write your MySQL query statement below
SELECT name FROM Employee e
WHERE e.id IN (
    SELECT managerId FROM Employee
    GROUP BY managerId
    HAVING count(*) >= 5
);


select a.Name
from Employee a
join Employee b
on a.Id = b.ManagerId
group by a.Name
having count(b.Name) >= 5;


SELECT
    Name
FROM
    Employee AS t1 JOIN
    (SELECT
        ManagerId
    FROM
        Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >= 5) AS t2
    ON t1.Id = t2.ManagerId
;

# 作者：LeetCode
# 链接：https://leetcode.cn/problems/managers-with-at-least-5-direct-reports/solution/zhi-shao-you-5ming-zhi-jie-xia-shu-de-jing-li-by-l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。