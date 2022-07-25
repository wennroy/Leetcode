# OUTER JOIN 外连接方式

SELECT *
FROM Employees t1
         LEFT JOIN Salaries t2 ON t1.employee_id = t2.employee_id
UNION
SELECT *
FROM Employees t1
         RIGHT JOIN Salaries t2 ON t1.employee_id = t2.employee_id;

# {"headers": ["employee_id", "name", "employee_id", "salary"], "values": [[2, "Crew", null, null],
# [4, "Haven", 4, 63539], [5, "Kristian", 5, 76071], [null, null, 1, 22517]]}

# 个人解法

# Write your MySQL query statement below
SELECT t1.employee_id FROM Employees t1
LEFT JOIN Salaries t2 ON t1.employee_id = t2.employee_id
WHERE t2.salary IS NULL
UNION
SELECT t2.employee_id FROM Employees t1
RIGHT JOIN Salaries t2 ON t1.employee_id = t2.employee_id
WHERE t1.name IS NULL
ORDER BY employee_id
;


## FULL OUTER JOIN 还没理清
# 以下为实验部分，搞清UNION, OUTER JOIN 和 INNER JOIN LEFT JOIN RIGHT JOIN等的关系

DROP TABLE IF EXISTS Employees;
CREATE TABLE IF NOT EXISTS Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(255)
);

DROP TABLE IF EXISTS Salaries;
CREATE TABLE IF NOT EXISTS Salaries (
    employee_id INT PRIMARY KEY,
    salary INT
);

INSERT INTO Employees VALUES
        (2, 'Crew'),
        (4, 'Haven'),
        (5, 'Kristian'),
        (7, 'Roy');

INSERT INTO Salaries VALUES
        (5, 76071),
        (1, 22517),
        (4, 63539),
        (8, 23457);

## INNER JOIN

SELECT * FROM Employees E
INNER JOIN Salaries S on E.employee_id = S.employee_id;
# 4,Haven,4,63539
# 5,Kristian,5,76071

SELECT * FROM Employees E
RIGHT JOIN Salaries S on E.employee_id = S.employee_id;

# ,,1,22517
# 4,Haven,4,63539
# 5,Kristian,5,76071
# ,,8,23457


SELECT * FROM Employees E
LEFT JOIN Salaries S on E.employee_id = S.employee_id;

# 2,Crew,,
# 4,Haven,4,63539
# 5,Kristian,5,76071
# 7,Roy,,

SELECT * FROM Employees E
CROSS JOIN Salaries S on E.employee_id = S.employee_id;

# 4,Haven,4,63539
# 5,Kristian,5,76071


# UNION 单纯将表格并列起来
SELECT * FROM Employees E
UNION
SELECT * FROM Salaries S;

# 2,Crew
# 4,Haven
# 5,Kristian
# 7,Roy
# 1,22517
# 4,63539
# 5,76071
# 8,23457

# UNION 和 JOIN 的结合实现外连接

SELECT * FROM Employees E
LEFT JOIN Salaries S on E.employee_id = S.employee_id
UNION
SELECT * FROM Employees E
RIGHT JOIN Salaries S on E.employee_id = S.employee_id;

# E.employee_id, name, S.employee_id, salary
# 2,Crew,,
# 4,Haven,4,63539
# 5,Kristian,5,76071
# 7,Roy,,
# ,,1,22517
# ,,8,23457


# FULL OUTER JOIN mysql中没有该语句，但我们可以利用 LEFT JOIN和RIGHT JOIN 来实现

# 对UNION前后进行限制

SELECT E.employee_id FROM Employees E
LEFT JOIN Salaries S on E.employee_id = S.employee_id
WHERE S.salary IS NULL
UNION
SELECT S.employee_id FROM Employees E
RIGHT JOIN Salaries S on E.employee_id = S.employee_id
WHERE E.name IS NULL;

# 切记限制语句仅在自己的SELECT语句中起效，以下方法不行。
SELECT E.employee_id FROM Employees E
LEFT JOIN Salaries S on E.employee_id = S.employee_id
UNION
SELECT S.employee_id FROM Employees E
RIGHT JOIN Salaries S on E.employee_id = S.employee_id
WHERE E.name IS NULL OR S.salary IS NULL;