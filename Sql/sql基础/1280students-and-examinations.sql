# Write your MySQL query statement below
SELECT st.student_id, st.student_name, s.subject_name, IFNULL(t.attended_exams, 0) attended_exams FROM Students st
CROSS JOIN Subjects s
LEFT JOIN (
    SELECT student_id, subject_name, count(*) attended_exams FROM Examinations e
    GROUP BY student_id, subject_name
) AS t
ON t.student_id = st.student_id AND t.subject_name = s.subject_name
ORDER BY st.student_id, s.subject_name;


# 三表连接，这个感觉比我的清晰一些

SELECT a.student_id, a.student_name, b.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students a CROSS JOIN Subjects b
    LEFT JOIN Examinations e ON a.student_id = e.student_id AND b.subject_name = e.subject_name
GROUP BY a.student_id, b.subject_name
ORDER BY a.student_id, b.subject_name

# 作者：sjdes
# 链接：https://leetcode.cn/problems/students-and-examinations/solution/san-biao-lian-he-cha-xun-cross-join-left-join-by-s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。