# Write your MySQL query statement below
SELECT contest_id, ROUND(COUNT(r.user_id)/u.count_user*100,2) percentage FROM Register r,
(SELECT COUNT(user_id) count_user FROM Users) AS u
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;

# ROUND(x, 2) * 100 会在保留两位小数的情况下先四舍五入，然后*100，最后仍然保留两位小数。
# ROUND(x * 100, 2) 正常保留两位小数

# 33.00 和 33.33