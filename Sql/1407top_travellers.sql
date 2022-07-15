# Write your MySQL query statement below
SELECT u.name, SUM(IFNULL(r.distance, 0)) travelled_distance FROM Users u
LEFT JOIN Rides r
ON u.id = r. user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name ASC;

# Write your MySQL query statement below
select u.name,coalesce(sum(distance),0) as travelled_distance
from users u left join rides r on u.id = r.user_id
group by u.id
order by travelled_distance desc,u.name

# 作者：ba-jie-ai
# 链接：https://leetcode.cn/problems/top-travellers/solution/by-ba-jie-ai-bw56/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。