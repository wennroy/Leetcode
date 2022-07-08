# Write your MySQL query statement below

# CASE WHEN exp THEN col ELSE xxx
# REGEXP
select employee_id, case when employee_id % 2 = 1 and name not regexp('^M') then salary else 0 end as bonus
from Employees
ORDER BY employee_id
;

# IF(CONDITION, TRUE_VALUE, FALSE_VALUE)
# LEFT(x,a)
select employee_id, IF(employee_id % 2 != 0 and left(name,1) != 'M',salary,0) as bonus
from Employees
order by employee_id
;