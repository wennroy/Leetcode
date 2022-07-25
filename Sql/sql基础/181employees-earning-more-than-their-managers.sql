# Write your MySQL query statement below
# 这里不能增加DISTINCT，可能有同名的员工

SELECT e.name Employee FROM Employee e
LEFT JOIN Employee e2
ON e.managerId = e2.id
WHERE e.salary > e2.salary;

# 两年前的答案芜湖
# Write your MySQL query statement below
SELECT
    a.Name Employee
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary