# lru_cache方法
from functools import lru_cache
class Solution:
    @lru_cache(128)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.fib(n-2) + self.fib(n-1)) % 1000000007

# 记忆化递归方法
class Solution:
    def __init__(self):
        self.record = defaultdict(int)
    def fib(self, n: int) -> int:
        def F(n):
            if n == 0:
                return 0
            elif n <= 2:
                return 1
            elif self.record[n]:
                return self.record[n]
            else:
                self.record[n] = F(n-1) + F(n-2)
                return self.record[n]
        return F(n) % (1000000007)

# 动态规划数组
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            dp = [0] * (n+1)
            dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-2] + dp[i-1]
            return dp[-1] % 1000000007

