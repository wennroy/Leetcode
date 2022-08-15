# 原题 50
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            neg = True
            bin_n = bin(n)[3:]
        else:
            neg = False
            bin_n = bin(n)[2:]
        ans = 1
        for val in bin_n[::-1]:
            if val == '1':
                ans *= x
            x *= x

        return 1 / ans if neg else ans