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

# 位运算
# 利用位运算来模拟能达到的最远距离，一旦最后一位是1，则达到此处。
# 本质是一种BFS的过程

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if not amount:
            return 0
        # 将减法转换为除法进行运算
        # 一旦最低位为1，则说明找到解，停止运算
        dp = 1 << amount
        res = 0
        while dp:
            tmp = 0
            res += 1
            # 每一轮运算计算一遍dp除以2**i得到的所有可能解
            for coin in coins:
                # tmp用于存储运算的中间结果
                # dp >> coin 实际上是进行除法运算：dp//2**coin
                # 使用位运算“或”来保存全部除法运算结果中的‘1’，实现批量运算
                # ps:这也是二进制移位的一个神奇之处，大家可以手动模拟一下这个过程
                # tmp有点类似于能达到的最远距离
                tmp |= dp >> coin
            # 一旦末尾出现1，则返回结果
            if tmp & 1:
                return res
            # 将本轮运算的全部运算结果送入下一轮计算
            dp = tmp
        return -1

# 作者：CodeHard_LiveFun
# 链接：https://leetcode.cn/problems/coin-change/solution/by-codehard_livefun-uzn9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。