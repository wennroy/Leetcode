# 简单自连接拼接

# Write your MySQL query statement below
SELECT c1.seat_id FROM Cinema c1
LEFT JOIN Cinema c2
ON c1.seat_id = c2.seat_id + 1
LEFT JOIN Cinema c3
ON c1.seat_id = c3.seat_id - 1
WHERE c1.free = 1 AND (c2.free = 1 OR c3.free = 1)
ORDER BY c1.seat_id;


select
	distinct c1.seat_id
from cinema c1 join cinema c2
on abs(c1.seat_id - c2.seat_id) = 1 and c1.free = 1 and c2.free = 1
order by c1.seat_id;


# 利用当前表的ROW_NUMBER() 和 seat_id的差值来判断是否在同一个连续的座位上。
with temp as (
	select
		seat_id,
		seat_id - row_number() over() as k
	from cinema where free = 1
)
select seat_id from temp where k in (
	select k from temp group by k having count(*) >= 2
);


with temp as (
	select
		seat_id,
		case
			when @pre_free = free and free = 1 then @pre_seat_id
			when @pre_free:=free then @pre_seat_id:=seat_id
		end as k
	from cinema, (select @pre_free:=null, @pre_seat_id:=null) init
)
select seat_id from temp where k in (
	select k from temp group by k having count(*) >= 2
);


# 作者：uccs
# 链接：https://leetcode.cn/problems/consecutive-available-seats/solution/san-chong-fang-fa-jie-lian-xu-kong-yu-de-x1f4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。