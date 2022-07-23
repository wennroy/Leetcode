# 子查询
# 由于套了两层，所以在里面那层出现空的时候，SELECT会产生NULL，需要去NULL
# Write your MySQL query statement below
SELECT t.recommended_page FROM (
    SELECT DISTINCT IF(f.user1_id = 1, l1.page_id, l2.page_id) recommended_page
    FROM Friendship f
    LEFT JOIN Likes l1
    ON f.user2_id = l1.user_id
    LEFT JOIN Likes l2
    ON f.user1_id = l2.user_id
    WHERE (f.user1_id = 1 OR f.user2_id = 1)
) AS t
WHERE t.recommended_page NOT IN (
    SELECT page_id FROM Likes WHERE user_id = 1
) AND t.recommended_page IS NOT NULL;


# UNION ALL
SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE user_id IN (
    SELECT user1_id AS user_id FROM Friendship WHERE user2_id = 1
    UNION ALL
    SELECT user2_id AS user_id FROM Friendship WHERE user1_id = 1
) AND page_id NOT IN (
    SELECT page_id FROM Likes WHERE user_id = 1
);

# CASE WHEN
SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE user_id IN (
    SELECT (
        CASE
        WHEN user1_id = 1 then user2_id
        WHEN user2_id = 1 then user1_id
        END
    ) AS user_id
    FROM Friendship
    WHERE user1_id = 1 OR user2_id = 1
)  AND page_id NOT IN (
    SELECT page_id FROM Likes WHERE user_id = 1
);

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/page-recommendations/solution/ye-mian-tui-jian-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。