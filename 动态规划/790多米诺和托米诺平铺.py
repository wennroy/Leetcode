# 正常的动态规划，

MOD_NUM = 1e9 + 7

class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        elif n == 3:
            return 5
        dp = [[0] * 2 for _ in range(n)]
        dp[0] = [0, 1]
        dp[1] = [1, 2]
        dp[2] = [2, 5]
        for i in range(3, n):
            dp[i][0] = (dp[i - 3][1] + dp[i - 2][0] + dp[i - 2][1]) % MOD_NUM
            dp[i][1] = (dp[i - 3][1] + dp[i - 2][0] + dp[i - 2][1] + dp[i - 1][0] + dp[i - 1][1]) % MOD_NUM

        return int(dp[-1][1])


# 标答解法，思考的状态更多一些
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][3] = (((dp[i - 1][0] + dp[i - 1][1]) % MOD + dp[i - 1][2]) % MOD + dp[i - 1][3]) % MOD
        return dp[n][3]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/domino-and-tromino-tiling/solution/duo-mi-nuo-he-tuo-mi-nuo-ping-pu-by-leet-7n0j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。