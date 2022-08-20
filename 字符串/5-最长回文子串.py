# 两年前的双指针，现在可能过不了的O(n^2) + O(1)的做法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_s = ''
        max_len = 0
        n = len(s)
        for i in range(n):
            head = i
            tail = i
            cur_len = 1
            while head>=1 and tail <= n-2 and s[head-1] == s[tail+1]:
                head -= 1
                tail += 1
                cur_len +=2
            if cur_len > max_len:
                max_s = s[head:tail+1]
                max_len = cur_len
        #        print(max_s)
            cur_len = 2
            head = i
            tail = i + 1
            while head >= 1 and tail <= n-2 and s[head-1] == s[tail+1]:
                head -= 1
                tail += 1
                cur_len += 2
            if cur_len > max_len and i <= n-2 and s[i] == s[i+1]:
                max_s = s[head:tail+1]
                max_len = cur_len
        return max_s

# O(n)的巧方法，利用回文的特性

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            start = max(i - len(res) - 1, 0)
            temp = s[start: i + 1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res


# O(n^2)的经典DP

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / longest - palindromic - substring / solution / zui - chang - hui - wen - zi - chuan - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。