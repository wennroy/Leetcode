# 简单的REGEXP的运用
# https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/
# https://www.runoob.com/mysql/mysql-regexp.html

SELECT * FROM Patients
WHERE conditions REGEXP ' DIAB1|^DIAB1';

SELECT patient_id,patient_name,conditions
FROM Patients
WHERE conditions LIKE "% DIAB1%"
or conditions LIKE "DIAB1%"

# 对于第一种情况,用LIKE "DIAB1%" 就足以应对
# 对于第二种情况,用LIKE "% DIAB1%",因为是空格后面以DIAB1为前缀,切记在%和DIAB1之间加上空格,否则会报错
# 用OR运算符把两种情况的条件都写上,则本题成功解决。

# 作者：7ucid-cohen
# 链接：https://leetcode.cn/problems/patients-with-a-condition/solution/by-7ucid-cohen-qpnh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。