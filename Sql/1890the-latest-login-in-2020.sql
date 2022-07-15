# TIMESTAMP 比较
# Write your MySQL query statement below
SELECT user_id, MAX(time_stamp) last_stamp FROM Logins
WHERE time_stamp <= TIMESTAMP('2020-12-31 23:59:59') AND time_stamp >= TIMESTAMP('2020-01-01 00:00:00')
GROUP BY user_id;