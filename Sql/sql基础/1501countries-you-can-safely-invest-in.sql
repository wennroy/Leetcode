# 复杂JOIN和HAVING 结合

# Write your MySQL query statement below
SELECT c.name country
FROM Country c,
     (SELECT caller_id, callee_id, duration, c1.name c1, c2.name c2
      FROM Calls ca
               LEFT JOIN Person p1
                         ON p1.id = ca.caller_id
               LEFT JOIN Person p2
                         ON p2.id = ca.callee_id
               LEFT JOIN Country c1
                         ON LEFT(p1.phone_number, 3) = c1.country_code
               LEFT JOIN Country c2
                         ON LEFT(p2.phone_number, 3) = c2.country_code) AS t
GROUP BY c.name
HAVING SUM(IF(t.c1 = c.name, t.duration, 0) + IF(t.c2 = c.name, t.duration, 0)) /
       SUM(IF(t.c1 = c.name, 1, 0) + IF(t.c2 = c.name, 1, 0)) > AVG(t.duration);

# Write your MySQL query statement below

# 先选两遍
with a as (
    select caller_id caller, duration from Calls
    union all
    select callee_id caller, duration from Calls
)
select c.name country from a left join Person p on a.caller=p.id
left join Country c on left(p.phone_number, 3)=c.country_code
group by c.name
having avg(a.duration) > (select avg(duration) from a)


# 作者：ffzs
# 链接：https://leetcode.cn/problems/countries-you-can-safely-invest-in/solution/union-all-left-join-by-ffzs-s3rw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。