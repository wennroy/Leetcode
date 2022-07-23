# Write your MySQL query statement below
SELECT t.left_operand, t.operator, t.right_operand, CASE WHEN (t.operator = '=' AND t.left_val=t.right_val)
                                                    OR (t.operator = '<' AND t.left_val < t.right_val)
                                                    OR (t.operator = '>' AND t.left_val > t.right_val)
                                                    THEN "true" ELSE 'false' END AS value
FROM (
SELECT e.left_operand, e.operator, e.right_operand, v1.value left_val, v2.value right_val FROM Expressions e
LEFT JOIN Variables v1
ON v1.name = e.left_operand
LEFT JOIN Variables v2
ON v2.name = e.right_operand
) AS t;


# WITH temp AS
# Write your MySQL query statement below
with temp as
(
    select a.*, b.value as v1, c.value as v2 from Expressions a
    left join
    Variables b
    on a.left_operand = b.name
    left join
    Variables c
    on a.right_operand = c.name
)

select left_operand, operator, right_operand,
case when (operator = '>' and v1 > v2)
        or (operator = '<' and v1 < v2)
        or (operator = '=' and v1 = v2) then "true"
     else "false" end as "value"
from temp

# 作者：YZBoostForest
# 链接：https://leetcode.cn/problems/evaluate-boolean-expression/solution/case-when-by-yzboostforest-lcmc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。