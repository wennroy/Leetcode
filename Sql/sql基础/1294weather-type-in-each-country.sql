# Write your MySQL query statement below
SELECT country_name, CASE WHEN AVG(weather_state) >= 25 THEN 'Hot'
                        WHEN AVG(weather_state) <= 15 THEN 'Cold'
                        ELSE 'Warm' END weather_type
FROM Countries c
RIGHT JOIN Weather w
ON c.country_id = w.country_id
WHERE w.day between '2019-11-01' AND '2019-11-30'
GROUP BY c.country_id;