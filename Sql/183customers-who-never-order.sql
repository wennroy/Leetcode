# 左连接解决
SELECT Name Customers
FROM (Customers
LEFT JOIN Orders
ON Customers.Id=Orders.CustomerId)
WHERE CustomerId IS NULL;

# 官方使用 NOT IN

select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);

# 作者：LeetCode
# 链接：https://leetcode.cn/problems/customers-who-never-order/solution/cong-bu-ding-gou-de-ke-hu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。