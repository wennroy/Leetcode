# 又被三年前的我吊打了
# 慢速写法：利用LEFT JOIN 找出每个部门的max salary 然后再寻找与其相等的条数

# Write your MySQL query statement below
SELECT d.name Department, e1.name Employee, e1.salary Salary FROM Department d, Employee e1
LEFT JOIN (
    SELECT departmentId, max(salary) max_salary FROM Employee
    GROUP BY departmentId
    ) AS t
ON e1.departmentId = t.departmentId
WHERE e1.salary = t.max_salary AND e1.departmentId = d.id;


# 三年前的快速写法，利用 >= ALL来解决
# Write your MySQL query statement below
SELECT DISTINCT Department.Name Department,e1.Name Employee,e1.Salary Salary
FROM Department,Employee AS e1
WHERE e1.Salary>= ALL
    (SELECT e2.Salary FROM Employee AS e2
    WHERE e1.DepartmentId = e2.DepartmentId
    )
AND e1.DepartmentId = Department.Id;


# 标答也是使用寻找salary = MAX salary。这里使用的是两个字段的 IN
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
;

# 作者：LeetCode
# 链接：https://leetcode.cn/problems/department-highest-salary/solution/bu-men-gong-zi-zui-gao-de-yuan-gong-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。