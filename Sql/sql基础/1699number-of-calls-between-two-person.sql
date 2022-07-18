# Write your MySQL query statement below
SELECT
    person1,person2,
    count(*) call_count,
    sum(duration) total_duration
FROM (
SELECT
    IF(from_id>to_id, to_id, from_id) person1,
    IF(from_id>to_id,from_id,to_id) person2,
    duration
FROM calls
) c
GROUP BY
    person1, person2

# 作者：Jam007
# 链接：https://leetcode.cn/problems/number-of-calls-between-two-persons/solution/by-jam007-mvea/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。