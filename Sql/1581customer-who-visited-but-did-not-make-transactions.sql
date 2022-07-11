# NOT IN 和 GROUP BY的结合
SELECT customer_id, COUNT(customer_id) count_no_trans FROM Visits v
WHERE v.visit_id NOT IN (
    SELECT t.visit_id FROM Transactions t
)
GROUP BY customer_id;

# 左连接找NULL 和 GROUP BY的结合
select t1.customer_id, count(t1.visit_id) as count_no_trans
from Visits as t1
left outer join Transactions as t2
on t1.visit_id  = t2.visit_id
where t2.amount is null
group by t1.customer_id

# 作者：7ucid-cohen
# 链接：https://leetcode.cn/problems/customer-who-visited-but-did-not-make-any-transactions/solution/by-7ucid-cohen-vhjp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。