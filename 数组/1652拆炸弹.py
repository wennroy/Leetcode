# 循环数组，只需要再补充一个数组即可。
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        if k < 0:
            code.reverse()
        T = abs(k)
        n = len(code)
        dp = [0] * n
        code = code + code
        dp[0] = sum(code[1:T + 1])
        for i in range(1, n):
            dp[i] = dp[i - 1] + code[i + T] - code[i]
        return dp if k > 0 else dp[::-1]

# 前缀和
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        res = []
        n = len(code)
        code += code
        if k > 0:
            l, r = 1, k
        else:
            l, r = n + k, n - 1
        w = sum(code[l:r+1])
        for i in range(n):
            res.append(w)
            w -= code[l]
            w += code[r + 1]
            l, r = l + 1, r + 1
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/defuse-the-bomb/solution/chai-zha-dan-by-leetcode-solution-01x3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。