# 笨比穷举办法
class Solution:
    def cuttingRope(self, n: int) -> int:
        last_ans = 0
        for split_num in range(2,n+1):
            x = n // split_num
            num_large = n - x * split_num
            num_small = split_num - num_large
            ans = x ** num_small * (x+1) ** num_large
            if ans < last_ans:
                return last_ans
            else:
                last_ans = ans
        return ans

import math

# 直接求极值点，一阶ODE
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

# 作者：jyd
# 链接：https://leetcode.cn/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def cuttingRope(self, n: int) -> int:
        last_ans = 0
        for split_num in range(max(n//3,2),n+1):
            x = n // split_num
            num_large = n - x * split_num
            num_small = split_num - num_large
            ans = math.pow(x,num_small) * math.pow((x+1),num_large)
            if ans < last_ans:
                return int(last_ans)
            else:
                last_ans = ans

        return int(ans)