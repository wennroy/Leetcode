# LOWER UPPER 更改大小写
# LEFT(name, 1) RIGHT(name, 2) 左起前几个 右起几个
# SUBSTRING(name, pos, len) 子串

SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;

