# 哈！三年前的答案
# Write your MySQL query statement below
SELECT IFNULL((SELECT DISTINCT e1.Salary FROM Employee AS e1
WHERE 1=(
    SELECT count(DISTINCT e2.Salary) FROM Employee AS e2
    WHERE e1.Salary<e2.Salary)
),NULL) SecondHighestSalary;

# 草三年前的我还挺聪明？？找出了有多少个DISTINCT 的工资是小于最小工资的。
# 然而可以利用 ORDER BY Salary DESC LIMIT 1 OFFSET 1来解决这样的选择问题。
# Return ONLY 1 record, start on record 2 (1+1)


SELECT MAX(salary) SecondHighestSalary FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

# LIMIT 1 OFFSET 1
# SELECT NULL;
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
#
# 作者：LeetCode
# 链接：https://leetcode.cn/problems/second-highest-salary/solution/di-er-gao-de-xin-shui-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
