# Write your MySQL query statement below
SELECT s.school_id, IFNULL(min(e.score),-1) score FROM Schools s
LEFT JOIN Exam e
ON s.capacity >= e.student_count
GROUP BY s.school_id;


# 一个窗口函数写法
select school_id,score from(
select *,rank() over (partition by school_id order by student_count desc,score asc) as rn
from(
select school_id,capacity,coalesce(score,-1) as score,coalesce(student_count,-1) as student_count
from Schools t1
left join Exam t2
on t1.capacity >=t2.student_count
) t
) t where rn=1
;

# 作者：leo-klee
# 链接：https://leetcode.cn/problems/find-cutoff-score-for-each-school/solution/fen-bu-zou-jie-jue-jian-dan-yi-dong-by-l-bs2h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。