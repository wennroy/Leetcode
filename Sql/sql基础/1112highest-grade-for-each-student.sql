# 子查询
# Write your MySQL query statement below
SELECT e.student_id, min(e.course_id) course_id, e.grade FROM Enrollments e,
(
SELECT student_id, max(grade) grade FROM Enrollments
GROUP BY student_id
) AS t
WHERE e.student_id = t.student_id AND e.grade = t.grade
GROUP BY e.student_id
ORDER BY e.student_id, e.course_id;


# 窗口函数
# rank() : 阶梯排序-前两个是并列的1，接下来就是第3名
# dense_rank(): 连续排序-前两个是并列的1，接下来就是第2名
# row_number(): 不会出现重复的排序
# <窗口函数> over (partition by <分组列名> order by <排序列名>)

select student_id, course_id, grade
from (
    select student_id, course_id, grade,
    rank() over (partition by student_id order by grade desc, course_id asc ) as ranking
    from Enrollments
) t1
where ranking = 1
order by student_id

# 作者：JinZou
# 链接：https://leetcode.cn/problems/highest-grade-for-each-student/solution/chuang-kou-han-shu-ji-chong-pai-xu-de-qu-s0fa/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。