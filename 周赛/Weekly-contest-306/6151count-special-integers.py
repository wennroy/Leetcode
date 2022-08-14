# 原题，见力扣1012

from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        @cache
        def solve(upper):
            @cache
            def dp(pos: int, headzero: bool, bound: bool, status: int) -> int:
                if pos == 0:
                    return 1

                ans = 0
                hi = nums[pos - 1] if bound else 9
                for cur in range(hi + 1):
                    if headzero and cur == 0:
                        ans += dp(pos - 1, True, bound and cur == hi, status)
                    else:
                        if not (status & (1 << cur)):
                            ans += dp(pos - 1, False, bound and cur == hi, status | (1 << cur))
                return ans

            nums = []
            while upper > 0:
                nums.append(upper % 10)
                upper //= 10

            return dp(len(nums), True, True, 0)

        return solve(n) - solve(0)




from collections import Counter
from math import factorial


def A(m, n):
    return factorial(m) // factorial(m - n)


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:

        def g(prefix, n):
            # print(prefix, n)
            if prefix == '0':
                return sum(A(10, i) // 10 * 9 for i in range(1, n + 1))
            z = Counter(prefix)
            if any(j > 1 for _, j in z.items()):
                return 0
            return A(10 - len(z), n)

        s = str(n + 1)
        m = len(s)
        ret = 0
        for i in range(m):
            for j in '0123456789':
                if j >= s[i]:
                    break
                ret += g(s[:i] + j, m - i - 1)
        return n - ret

    def countSpecialNumbers(self, n: int) -> int:
        return n - self.numDupDigitsAtMostN(n)



class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        return N - self.F(N)

    def F(self, n: int) -> int:     #小于等于n的  没有重复digit的num 的 个数
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits = digits[::-1]       #从左至右 存储n的每一位上的数字
        k = len(digits)
        visited = [0 for _ in range(10)]                #记录从左至右 n用了几次了！！！！！！！！
        res = 0
        # 前面是0的情况 0XXXXX  00XXXXX  000XXXX 00000XXX 有效数字的位数自然就是k-1 ~ 1位
        for i in range(1, k):
            res += 9 * self.A(i-1 , 9)   #有效的i位中，首位有1~9 共9种选择  后面的i-1位是从9中挑选（i-1）种  有序排列
        #前面没有0
        for i in range(0, k):   #n从左至右遍历
            num = digits[i]
            min_digit = 1 if i == 0 else 0
            for x in range(min_digit, num): # 4567   选择第0位  第0位可选的数在1~3中选择  选择第1位  可选的数为0~4（4）
                if visited[x] == 0:                 #n没用过！！！！！！！！！！！
                    res += self.A(k-i-1, 10-i-1);
            visited[num] += 1
            if visited[num] > 1:            #4456  整理完44以后，就不用整理了  4400~4456一定是有重复的
                break
            if i == k-1:                    #我们都是让x比num小，如果一直到最后一位了，n本身也算一个的
                res += 1
        return res

    def fact(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * self.fact(n - 1)
    def A(self, m: int, n: int) -> int:
        return self.fact(n) // self.fact(n - m)

# 作者：XingHe_XingHe
# 链接：https://leetcode.cn/problems/numbers-with-repeated-digits/solution/cpython3-fen-qing-kuang-tao-lun-n-bu-zho-t0ge/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 拆分出来计算，先计算无重复部分，然后计算重复部分。
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        # 考虑无重复数字的个数
        # N + 1避免单独处理N
        nums = list(map(int, str(N + 1)))
        ans = 0

        # 计算排列数
        def A(m, n):
            return 1 if n == 0 else A(m, n - 1) * (m - n + 1)

        # 计算位数小于N的无重复数字个数
        for i in range(1, len(nums)):
            ans += 9 * A(9, i - 1)

        c = set()
        for digit, num in enumerate(nums):
            # 计算当前位数上的可用数字数量(首位不能为0)
            usenumber = sum(i not in c for i in range(0 if digit else 1, num))
            ans += usenumber * A(10 - digit - 1, len(nums) - digit - 1)
            # 若当前数字存在重复
            if num in c:
                break
            c.add(num)
        return N - ans


# 作者：已注销
# 链接：https: // leetcode.cn / problems / numbers -
# with-repeated - digits / solution / pai - lie - shu - qiu - jie - by - wzhaooooo /
#     来源：力扣（LeetCode）
#     著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    import time
    n = 10**9
    cur_time = time.time()
    k = Solution()
    print(k.countSpecialNumbers(n))
    print(f'time elapsed: {time.time() - cur_time}s')