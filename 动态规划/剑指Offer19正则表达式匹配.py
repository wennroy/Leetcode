class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = list(map(str, s))
        p = list(map(str, p))
        if s == [] and p == []:
            return True
        if (s == [] and p != []) or (s != [] and p == []):
            return False

        while s != []:
            print(s, p)
            if len(p) == 0:
                return False
            elif len(p) == 1:
                if len(s) == 1 and (p[0] == s[0] or p[0] == '.'):
                    return True
                else:
                    return False
            elif len(p) >= 2:
                if (p[0] != s[0] or p[0] == '.') and p[1] != '*':
                    return False
                elif (p[0] == s[0] or p[0] == '.') and p[1] != '*':
                    p.pop(0)
                    s.pop(0)
                elif (p[0] != s[0] and p[0] != '.') and p[1] == '*':
                    p.pop(0)
                    p.pop(0)
                elif (p[0] == s[0] or p[0] == '.') and p[1] == '*':
                    s.pop(0)

        if s == []:
            if len(p) == 0:
                return True
            elif len(p) == 2 and p[1] == '*':
                return True
            else:
                return False


# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]    # 代表从s[:i]到p[:j]可以匹配

        dp[0][0] = True
        # p 如果都是 'a*' x n 就能匹配空的字符串，返回正确
        for j in range(2, m+1):
            if p[j-1] == '*' and dp[0][j-2] == True:
                dp[0][j] = True

        # 转移方程： 进行到第i, j时，匹配s[:i]和p[:j]
        # 如果 s[i-1] == p[j-1] 或者 p[j-1] == '.'  且 dp[i-1][j-1] = True => True
        # 如果 p[j-2] == '*' 且 p[j-1] == s[i-1] 或 p[j-1] == '.' 且 dp[i-1][j-2] = True => True
        for i in range(n+1):
            for j in range(m+1):
                if i >=1 and j >= 1 and (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]:
                    dp[i][j] = True
                if i>=1 and j>=2 and p[j-1] == '*' and (p[j-2] == s[i-1] or p[j-2] == '.') and (dp[i-1][j-2] or dp[i-1][j]):
                    dp[i][j] = True
                if j >= 2 and p[j-1] == '*' and dp[i][j-2]:
                    print(i, j)
                    dp[i][j] = True
        # print(dp)
        return dp[-1][-1]

# TFTFTF
# FFFTFF
# FFFFFF
# FFFFFF


if __name__ == '__main__':
    sol = Solution()
    s = 'aaa'
    p = 'a.a'
    sol.isMatch(s, p)