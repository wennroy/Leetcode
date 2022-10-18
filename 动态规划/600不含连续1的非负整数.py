# 数位DP方法，时间复杂度为O(log(n))，总共状态有logn个，只在i与i-1的状态上转移，所以时间复杂度是O(logn*2) = O(logn)
from functools import cache
class Solution:
    def findIntegers(self, n: int) -> int:
        # 数位DP
        s = bin(n)[2:]
        @cache
        def f(i: int, isOne: bool, isLimit: bool):
            if i == len(s):
                return 1
            res = 0
            up = int(s[i]) if isLimit else 1
            res += f(i+1, False, isLimit and 0==up)
            if not isOne and up == 1:
                res += f(i+1, True, isLimit)

            return res

        return f(0, False, True)

if __name__ == '__main__':
    sol = Solution()
    n = 5
    print(sol.findIntegers(n))


