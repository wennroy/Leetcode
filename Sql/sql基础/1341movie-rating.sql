# Write your MySQL query statement below
with temp1 as(
    SELECT user_id, rank() over(order by count(*) DESC) count_review FROM MovieRating
    GROUP BY user_id
), temp2 as(
    SELECT movie_id, rank() over(order by avg(rating) DESC) rating_review FROM MovieRating
    WHERE MONTH(created_at) = 2
    GROUP BY movie_id
)

(SELECT u.name results FROM Users u
INNER JOIN temp1 t1
ON u.user_id = t1.user_id
WHERE t1.count_review = 1
ORDER BY u.name LIMIT 1)
UNION ALL
(SELECT m.title results FROM Movies m
INNER JOIN temp2 t2
ON m.movie_id = t2.movie_id
WHERE t2.rating_review = 1
ORDER BY m.title LIMIT 1)


# Write your MySQL query statement below
(
    select u.name as results
    from MovieRating r join Users u
    on r.user_id=u.user_id
    group by r.user_id
    order by count(r.movie_id) desc, u.name
    limit 0,1
)
union all
(
    select m.title as results
    from MovieRating r join Movies m
    on r.movie_id=m.movie_id
    where r.created_at between '2020-02-01' and '2020-02-29'
    group by r.movie_id
    order by avg(r.rating) desc, m.title
    limit 0,1
)
;

# 作者：cmite
# 链接：https://leetcode.cn/problems/movie-rating/solution/by-cmite-frbw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。