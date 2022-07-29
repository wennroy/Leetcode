class Solution:
    def myPow(self, x: float, n: int) -> float:
        stack = []
        sign = 1
        if n == 0:
            return 1

        if n < 0:
            sign = -1
            n = -n
        while n > 1:
            if n % 2 == 0:
                stack.append(0)
            else:
                stack.append(1)
            n = n // 2
        ans = x
        while stack:
            ans *= ans * x ** stack.pop()
        if sign == -1:
            ans = 1 / ans
        return ans

# 标答方法1：快速幂加递归，基本一致。我利用stack来存储每个值，而标答直接递归

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

# 标答方法2：快速幂+迭代：二进制迭代法。以n = 77举例，用二进制来表示77，即可得到我们所需的乘子。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

#
# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / powx - n / solution / powx - n - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。