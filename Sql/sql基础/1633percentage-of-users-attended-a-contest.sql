# Write your MySQL query statement below
SELECT contest_id, ROUND(COUNT(r.user_id)/u.count_user*100,2) percentage FROM Register r,
(SELECT COUNT(user_id) count_user FROM Users) AS u
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;

# ROUND(x, 2) * 100 会在保留两位小数的情况下先四舍五入，然后*100，最后仍然保留两位小数。
# ROUND(x * 100, 2) 正常保留两位小数

# 33.00 和 33.33

select contest_id,round(count(user_id) / (select count(1) from Users) * 100, 2) as percentage
from Register
group by contest_id
order by percentage desc,contest_id

# 作者：erke
# 链接：https://leetcode.cn/problems/percentage-of-users-attended-a-contest/solution/roundcountuser_id-select-count1-from-use-amzh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。