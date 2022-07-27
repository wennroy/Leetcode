# Write your MySQL query statement below
with temp as(
    SELECT client_id, driver_id, status, request_at FROM Trips t
    INNER JOIN Users u1
    ON t.client_id = u1.users_id
    INNER JOIN Users u2
    ON t.driver_id = u2.users_id
    WHERE request_at between '2013-10-01' AND '2013-10-03' AND (u1.banned != 'Yes' AND u2.banned != 'Yes')
), temp2 as(
    SELECT request_at, COUNT(*) count_total FROM temp GROUP BY request_at
), temp3 as(
    SELECT temp2.request_at, ROUND(count(*) / temp2.count_total, 2) cancelled FROM temp2
    LEFT JOIN temp t
    ON temp2.request_at = t.request_at
    WHERE t.status != 'completed'
    GROUP BY t.request_at
)
SELECT temp2.request_at Day, COALESCE(t3.cancelled, 0.00) 'Cancellation Rate' FROM temp2
LEFT JOIN temp3 AS t3
ON temp2.request_at = t3.request_at;

# 解法一
SELECT T.request_at AS `Day`,
	ROUND(
			SUM(
				IF(T.STATUS = 'completed',0,1)
			)
			/
			COUNT(T.STATUS),
			2
	) AS `Cancellation Rate`
FROM Trips AS T
JOIN Users AS U1 ON (T.client_id = U1.users_id AND U1.banned ='No')
JOIN Users AS U2 ON (T.driver_id = U2.users_id AND U2.banned ='No')
WHERE T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at

# 解法二
SELECT T.request_at AS `Day`,
	ROUND(
			SUM(
				IF(T.STATUS = 'completed',0,1)
			)
			/
			COUNT(T.STATUS),
			2
	) AS `Cancellation Rate`
FROM trips AS T LEFT JOIN
(
	SELECT users_id
	FROM users
	WHERE banned = 'Yes'
) AS A ON (T.Client_Id = A.users_id)
LEFT JOIN (
	SELECT users_id
	FROM users
	WHERE banned = 'Yes'
) AS A1
ON (T.Driver_Id = A1.users_id)
WHERE A.users_id IS NULL AND A1.users_id IS NULL AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at

# 解法三
SELECT T.request_at AS `Day`,
	ROUND(
			SUM(
				IF(T.STATUS = 'completed',0,1)
			)
			/
			COUNT(T.STATUS),
			2
	) AS `Cancellation Rate`
FROM trips AS T
WHERE
T.Client_Id NOT IN (
	SELECT users_id
	FROM users
	WHERE banned = 'Yes'
)
AND
T.Driver_Id NOT IN (
	SELECT users_id
	FROM users
	WHERE banned = 'Yes'
)
AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at

#
# 作者：jason-2
# 链接：https://leetcode.cn/problems/trips-and-users/solution/san-chong-jie-fa-cong-nan-dao-yi-zong-you-gua-he-n/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。