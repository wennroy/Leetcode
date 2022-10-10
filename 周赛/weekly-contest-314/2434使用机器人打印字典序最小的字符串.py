# 栈模拟+贪心 本质还是个模拟过程
from collections import defaultdict
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        record = defaultdict(list)
        for i, val in enumerate(s):
            val = ord(val) - ord("a")
            record[val].append(i)

        j = -1
        stack = []
        ans = []
        for i in range(26):
            if not record[i] or record[i][-1] <= j:
                continue
            for k in range(j + 1, record[i][-1] + 1):
                while stack and ord(stack[-1]) - ord("a") <= i:
                    ans.append(stack.pop())
                stack.append(s[k])
            j = record[i][-1]
        ans += stack[::-1]
        return ''.join(ans)
