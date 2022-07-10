# 又做到了三年前做过的题呢，但是完全忘光了呢md
# 删除重复出现的内容

DELETE p1 FROM Person p1, Person p2
WHERE p1.email = p2.email
AND p1.id > p2.id;

# 将SELECT改成DELETE即可
# SELECT p1.* FROM Person p1, Person p2
# WHERE p1.email = p2.email
# AND p1.id > p2.id;
