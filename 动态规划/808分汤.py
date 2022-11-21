# 一道经典动态规划题目，一定要敢于相信On2的方法是正确的

class Solution:
    def soupServings(self, n: int) -> float:
        from functools import cache
        N = (n + 24) // 25

        @cache
        def travel(A, B):
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0:
                return 1
            if B <= 0:
                return 0

            return (travel(A - 4, B) + travel(A - 3, B - 1) + travel(A - 2, B - 2) + travel(A - 1, B - 3)) / 4

        return travel(N, N)

# dp
class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        if n >= 179:
            return 1.0
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0] = [0.5] + [1.0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] +
                            dp[max(0, i - 2)][max(0, j - 2)] + dp[max(0, i - 1)][max(0, j - 3)]) / 4
        return dp[n][n]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/soup-servings/solution/fen-tang-by-leetcode-solution-0yxs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    sol = Solution()
    import time
    for i in range(0,5001,25):
        start_time = time.time()
        k = sol.soupServings(i)
        print(f"Elapsed Time: {time.time() - start_time} for {i}: {k}")
