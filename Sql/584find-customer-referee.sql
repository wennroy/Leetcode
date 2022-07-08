# 首先是几种不等于的方法，均是可以的
SELECT name
FROM customer
WHERE referee_id <> 2 OR referee_id IS NULL;

SELECT name
FROM customer
WHERE !(referee_id = 2) OR referee_id IS NULL;

SELECT name
FROM customer
WHERE referee_id != 2 OR referee_id IS NULL;

# 这一题的主要考点是 MySQL 使用三值逻辑 —— TRUE, FALSE 和 UNKNOWN。
# 任何与 NULL 值进行比较都会与第三种值 UNKNOWN 进行比较，因此需要额外加入 IS NULL。

# 以下方法会在第六个案例中出错。 UNION约等于是取并集，因此并不是完全与OR相等
# 相同字符段的并集会只留下一个结果。有点类似于UNIQUE但又不同。
SELECT name
FROM customer
WHERE referee_id IS NULL

UNION

SELECT name
FROM customer
WHERE referee_id <> 2;