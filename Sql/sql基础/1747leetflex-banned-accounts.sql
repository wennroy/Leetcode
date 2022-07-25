# Write your MySQL query statement below
# 依然是简单自连接，想清楚逻辑就很快了
SELECT DISTINCT l1.account_id FROM LogInfo l1, LogInfo l2
WHERE l1.account_id = l2.account_id AND l1.ip_address != l2.ip_address
AND l2.logout >= l1.login AND l2.login <= l1.logout;
