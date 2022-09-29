# 数学方法
from typing import List
from math import sqrt
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_val = sum(nums)
        n = n + 2
        # 平方和公式
        # n(n+1)(2n+1) / 6

        sum_squared = n * (n + 1) * (2 * n + 1) // 6
        num_squared = 0
        for num in nums:
            num_squared += num ** 2

        two_sum = (1 + n) * n // 2 - sum_val
        two_squared_sum = sum_squared - num_squared

        delta = 2 * two_squared_sum - two_sum ** 2
        sqrt_delta = sqrt(delta)
        ans = [(two_sum - sqrt_delta) // 2, (two_sum + sqrt_delta) // 2]
        return list(map(int, ans))

# 位运算
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        xorsum = 0
        n = len(nums) + 2
        for num in nums:
            xorsum ^= num
        for i in range(1, n + 1):
            xorsum ^= i

        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                type1 ^= i
            else:
                type2 ^= i

        return [type1, type2]


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / missing - two - lcci / solution / xiao - shi - de - liang - ge - shu - zi - by - leetcode - zuwq3 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。