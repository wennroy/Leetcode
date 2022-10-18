# 依旧是数位DP
from functools import cache
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, mask: int, isLimit: bool, isNum: bool):
            if i == len(s):
                return int(isNum)
            res = 0
            if not isNum:
                res += f(i + 1, mask, False, False)
            up = int(s[i]) if isLimit else 9
            for d in range(0 if isNum else 1, up + 1):
                if mask >> d & 1 == 0:
                    res += f(i + 1, mask | (1 << d), isLimit and up == d, True)

            return res

        return n - f(0, 0, True, False)