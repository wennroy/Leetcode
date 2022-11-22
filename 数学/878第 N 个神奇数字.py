# 二分法
import math

MOD = 10 ** 9 + 7

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        _lcm = math.lcm(a, b)

        def check(x):
            return x // a + x // b - x // _lcm

        left, right = 2, 10 ** 18
        while left <= right:
            mid = left + ((right - left) >> 1)
            if check(mid) >= n:
                right = mid - 1
            else:
                left = mid + 1
        return left % MOD


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        l = min(a, b)
        r = n * min(a, b)
        c = lcm(a, b)
        while l <= r:
            mid = (l + r) // 2
            cnt = mid // a + mid // b - mid // c
            if cnt >= n:
                r = mid - 1
            else:
                l = mid + 1
        return (r + 1) % MOD

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/nth-magical-number/solution/di-n-ge-shen-qi-shu-zi-by-leetcode-solut-6vyy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 找规律
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        c = lcm(a, b)
        m = c // a + c // b - 1
        r = n % m
        res = c * (n // m) % MOD
        if r == 0:
            return res
        addA = a
        addB = b
        for _ in range(r - 1):
            if addA < addB:
                addA += a
            else:
                addB += b
        return (res + min(addA, addB) % MOD) % MOD

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/nth-magical-number/solution/di-n-ge-shen-qi-shu-zi-by-leetcode-solut-6vyy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。