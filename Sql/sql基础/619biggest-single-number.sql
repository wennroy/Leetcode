# Write your MySQL query statement below
SELECT (SELECT num
        FROM MyNumbers m
        GROUP BY num
        HAVING COUNT(num) < 2
        ORDER BY num DESC
        LIMIT 1) num;

# 因为SQL在执行时是按照 FROM -> ON -> OUTER(JOIN) -> WHERE -> GROUP BY　->　HAVING -> SELECT -> DISTINCT -> ORDER BY -> limit 这个执行顺序执行的，所以如果写成下面两种写法会先执行
# from my_numbers
# group by num
# having count(*) = 1
# 然后再执行 select ifnull(num, null) 或者 select num,但是因为先执行了查询，当having count(*) = 1 返回空时，这时结果集中没有数据，在执行select时，便不会去调用ifnull()函数，
# 最后再执行 limit 1， limit 1若无数据，则会返回空，而不是NULL

# 作者：heavenwalker
# 链接：https://leetcode.cn/problems/biggest-single-number/solution/619-ifnullyong-fa-zhu-yi-shi-xiang-jie-g-rfrd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。