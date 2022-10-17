from typing import List
from functools import cache
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        digits = list(map(int, digits))
        @cache
        def f(i: int, isLimit: bool, isNum:bool) -> int:
            if i == len(s):
                return int(isNum)
            res = 0
            if not isNum:
                res += f(i+1, False, False)
            up = int(s[i]) if isLimit else 9
            for d in digits:
                if d <= up:
                    res += f(i + 1, isLimit and up == d, True)
            return res

        return f(0, True, False)

if __name__ == '__main__':
    digits = ["1","2","3","4","7","8","9"]
    n = 32901345
    sol = Solution()
    print(sol.atMostNGivenDigitSet(digits, n))
