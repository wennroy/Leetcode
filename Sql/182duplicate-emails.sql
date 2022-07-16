# Duplicate emails
# 三年后的退化版本xs 自连结
SELECT DISTINCT p1.Email FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.Id != p2.Id;

# 知道使用group by和 having。还需要记得优先顺序。where>group by>having>order by
# 三年前的版本
select Email from Person group by Email having count(Email)>1;


select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
;
# 作者：LeetCode
# 链接：https://leetcode.cn/problems/duplicate-emails/solution/cha-zhao-zhong-fu-de-dian-zi-you-xiang-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。