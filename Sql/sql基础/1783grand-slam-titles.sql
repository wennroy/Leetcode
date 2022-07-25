# CROSS JOIN 找出所有
# Write your MySQL query statement below
SELECT player_id, player_name, SUM(IF(player_id = c.Wimbledon, 1, 0)+
                                    IF(player_id = c.Fr_open, 1, 0)+
                                    IF(player_id = c.US_open, 1, 0)+
                                    IF(player_id = c.Au_open, 1, 0)) grand_slams_count
FROM Players p
CROSS JOIN Championships c
GROUP BY player_id
HAVING grand_slams_count != 0;

