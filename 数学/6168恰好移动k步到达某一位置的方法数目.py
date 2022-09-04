# 数学题，推出组合数表达式就算完成了。

from math import factorial


class Solution:
    def C(self, x, n):
        # 组合数 C_n^x
        return factorial(n) // factorial(n - x) // factorial(x)

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        distance = abs(startPos - endPos)
        if distance > k or distance % 2 != k % 2:
            return 0

        # 组合数，总共你能动k步，其中有x步你要前进，剩下的k-x步你要后退etc.
        x = (k + distance) // 2
        return int(self.C(x, k) % (10 ** 9 + 7))