select round((select count(player_id) from (
	select
		player_id,
		event_date,
		lag(event_date)
			over(partition by player_id order by event_date) as next_date,
		rank() over(partition by player_id order by event_date) as login_times
	from activity
) as temp where datediff(event_date, next_date) = 1 and login_times = 2)
/
(select count(player_id) from (
	select player_id from activity group by player_id
) as temp), 2) as fraction;



select round((
	(select count(player_id) from (
		select
			player_id,
			datediff(event_date, min(event_date) over(partition by player_id)) as diff
		from activity
	) as temp where diff = 1) / (select count(distinct player_id) from activity)
), 2) as fraction;



with temp as (
	select
		player_id,
		datediff(event_date, min(event_date) over(partition by player_id)) as diff
	from activity
) select round(
	sum(case diff when 1 then 1 else 0 end) /
	count(distinct player_id),
2) as fraction from temp;



select round(avg(event_date is not null), 2) as fraction from (
	select player_id, min(event_date) as first_login from activity
	group by player_id
) temp left join activity
on temp.player_id = activity.player_id
and datediff(event_date, first_login) = 1;

# 作者：uccs
# 链接：https://leetcode.cn/problems/game-play-analysis-iv/solution/cong-xiao-bai-shi-jiao-yong-4-chong-fang-su4b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。