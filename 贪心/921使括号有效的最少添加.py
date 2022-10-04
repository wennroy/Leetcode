# 简单贪心
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        ans = 0
        for l in s:
            if l == '(':
                cnt += 1
            elif l == ')':
                cnt -= 1

            if cnt < 0:
                ans += 1
                cnt = 0

        return ans + cnt
