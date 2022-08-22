# 动态规划，寻找对应的转换关系，又写了快一个小时，废了

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]  # 第0,0位为空字符对空字符，永远是True
        dp[0][0] = True
        for j in range(1, m+1):
            if p[j-1] == '*' and dp[0][j-2]:
                dp[0][j] = True
        for i in range(1,n+1):
            for j in range(1, m+1):
                if (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]:
                    dp[i][j] = True
                elif p[j-1] == '*': # 是*号的情况，分情况讨论
                    if (dp[i-1][j-1] or dp[i-1][j]) and (s[i-1] == p[j-2] or p[j-2] == '.'):    # 前一格相同，我们就可以有好多个相同的。
                        dp[i][j] = True
                    elif dp[i][j-2]:  # 前两格还是相同，则这个数字可能可以不取
                        dp[i][j] = True
        print(dp)
        return dp[-1][-1]



# 标答：标答思路比较清晰。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。