# Write your MySQL query statement below
# 有个小坑 https://blog.csdn.net/ispringmw/article/details/109697504
# 在查询的时候，NOT IN块若这么写将会返回空值，因为SELECT中选取的值含有NULL
# WHERE id NOT IN (
#     SELECT DISTINCT p_id FROM tree
# )

SELECT id, 'Root' AS Type FROM tree
WHERE p_id IS NULL
UNION
SELECT id, 'Leaf' AS Type FROM tree
WHERE id NOT IN (
    SELECT DISTINCT p_id FROM tree
    WHERE p_id IS NOT NULL
) AND p_id IS NOT NULL
UNION
SELECT id, 'Inner' AS Type FROM tree
WHERE id IN (
    SELECT DISTINCT p_id FROM tree
    WHERE p_id IS NOT NULL
) AND p_id IS NOT NULL
ORDER BY id;

# 第二种办法，利用CASE语句
SELECT
    id AS `Id`,
    CASE
        WHEN tree.id = (SELECT atree.id FROM tree atree WHERE atree.p_id IS NULL)
          THEN 'Root'
        WHEN tree.id IN (SELECT atree.p_id FROM tree atree)
          THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM
    tree
ORDER BY `Id`
;

# Write your MySQL query statement below
select id ,
Case
When p_id is null Then "Root"
When id  in (select distinct p_id from tree) Then "Inner"
Else "Leaf"
End Type
from tree;


# 作者：LeetCode
# 链接：https://leetcode.cn/problems/tree-node/solution/shu-jie-dian-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 第三种办法，利用IF

SELECT
    atree.id,
    IF(ISNULL(atree.p_id),
        'Root',
        IF(atree.id IN (SELECT p_id FROM tree), 'Inner','Leaf')) Type
FROM
    tree atree
ORDER BY atree.id
