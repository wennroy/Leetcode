# 很有意思的一道题，讲列前后错开，就能在同一行找到我们所需要的数据了
# Write your MySQL query statement below
SELECT s1.id,
       IFNULL(IF(s1.id % 2 = 1, s2.student, s3.student), (SELECT student
                                                          FROM Seat
                                                          ORDER BY id DESC
                                                          LIMIT 1)) student
FROM Seat s1
         LEFT JOIN Seat s2
                   ON s1.id + 1 = s2.id
         LEFT JOIN Seat s3
                   ON s1.id - 1 = s3.id;

# 标答利用 CASE 修改ID，最后 ORDER
SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seat,
    (SELECT
        COUNT(*) AS counts
    FROM
        seat) AS seat_counts
ORDER BY id ASC;

# 位操作和 COALESCE()
SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id;


# 作者：LeetCode
# 链接：https://leetcode.cn/problems/exchange-seats/solution/huan-zuo-wei-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 异或^的理解，0^0=0 0^1=1 1^0=1 1^1=0  (s1.id + 1) ^ 1) - 1