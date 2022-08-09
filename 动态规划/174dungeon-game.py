# 倒序的动态规划，这样才能保证骑士不会死
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 陷入死局的动态规划
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]  # [0, 0]当前的能保存的最大血量，之前到达的最小的最大血量
        dp[0][0] = [dungeon[0][0], dungeon[0][0]]
        for j in range(1, n):
            dp[0][j][0] = dp[0][j - 1][0] + dungeon[0][j]
            dp[0][j][1] = min(dp[0][j - 1][1], dp[0][j][0])
        for i in range(1, m):
            dp[i][0][0] = dp[i - 1][0][0] + dungeon[i][0]
            dp[i][0][1] = min(dp[i - 1][0][1], dp[i][0][0])

        for j in range(1, n):
            for i in range(1, m):
                temp_list = [min(dp[i - 1][j][0] + dungeon[i][j], dp[i - 1][j][1]),
                             min(dp[i][j - 1][0] + dungeon[i][j], dp[i][j - 1][1])]
                if temp_list[0] >= temp_list[1]:
                    dp[i][j][0] = dp[i - 1][j][0] + dungeon[i][j]
                    dp[i][j][1] = temp_list[0]
                else:
                    dp[i][j][0] = dp[i][j - 1][0] + dungeon[i][j]
                    dp[i][j][1] = temp_list[1]
        print(dp)
        return -dp[-1][-1][1] + 1 if dp[-1][-1][1] <= 0 else 1
