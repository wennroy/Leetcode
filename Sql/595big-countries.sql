-- 方案一，选用OR来通过

SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000;

-- 方案二：利用UNION连接子查询

SELECT
    name, population, area
FROM
    world
WHERE
    area >= 3000000

UNION

SELECT
    name, population, area
FROM
    world
WHERE
    population >= 25000000
;

-- 方案二会比方案一来的快，但总体没有太大区别。

