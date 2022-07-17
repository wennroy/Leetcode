# 秒了，HAVING COUNT
# 执行顺序问题，需注意 WHERE > GROUP BY > HAVING > ORDER BY
# 因此不能使用 WHERE

# Write your MySQL query statement below
SELECT actor_id, director_id FROM ActorDirector
GROUP BY actor_id, director_id
HAVING
COUNT(*) >= 3;