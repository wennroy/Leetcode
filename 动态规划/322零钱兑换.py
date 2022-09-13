from typing import List
from math import inf
# 纯递归，超时
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1

        coins.sort()
        max_val = coins[-1]
        max_coin = amount // max_val
        min_coin = inf
        for i in range(max_coin + 1):
            next_coin = self.coinChange(coins[:-1], amount - max_val * i)
            if next_coin != -1:
                min_coin = min(min_coin, i + next_coin)

        return min_coin if min_coin != inf else -1


# 递归+部分剪枝，超时
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return -1

        coins.sort()
        max_val = coins[-1]
        max_coin = amount // max_val
        min_coin = inf
        for i in range(max_coin, -1, -1):
            next_coin = self.coinChange(coins[:-1], amount - max_val * i)
            if next_coin != -1:
                min_coin = min(min_coin, i + next_coin)

        return min_coin if min_coin != inf else -1

# 记忆化递归
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(amount)
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)

# dp 直接遍历
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / coin - change / solution / 322 - ling - qian - dui - huan - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。