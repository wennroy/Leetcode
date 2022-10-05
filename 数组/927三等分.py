# 强行计算法：将1的数量三等分，通过前置0和后置0筛选剪枝
# 最后对三个数组进行比较，时间复杂度较难计算，由于存在两个循环，可能最差情况在O(n2)

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        sum_arr = [arr[0]]
        n = len(arr)
        for num in arr[1:]:
            sum_arr.append(sum_arr[-1] + num)
        if sum_arr[-1] == 0:
            return [0, 2]
        elif sum_arr[-1] % 3 != 0:
            return [-1, -1]
        # print(sum_arr)
        one_third = sum_arr[-1] // 3
        first_low = bisect_left(sum_arr, one_third)
        first_up = bisect_right(sum_arr, one_third)

        second_low = bisect_left(sum_arr, one_third * 2)
        second_up = bisect_right(sum_arr, one_third * 2)

        # print(first_low, first_up, second_low, second_up)

        i = 0  # 第一位数的前置0
        while arr[i] == 0:
            i += 1

        j = n - 1  # 最后的后置0
        while arr[j] == 0:
            j -= 1
        houzhi = n - 1 - j  # 后置0的个数

        for first in range(first_low + houzhi, first_up):
            for second in range(second_low + houzhi, second_up):
                if arr[i:first + 1] == arr[second_up:] == arr[first_up:second + 1]:
                    return [first, second + 1]

        return [-1, -1]


# 标答真正做到了O(n)，可以直接从first second third的位置检测
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        s = sum(arr)
        if s % 3:
            return [-1, -1]
        if s == 0:
            return [0, 2]

        partial = s // 3
        first = second = third = cur = 0
        for i, x in enumerate(arr):
            if x:
                if cur == 0:
                    first = i
                elif cur == partial:
                    second = i
                elif cur == 2 * partial:
                    third = i
                cur += 1

        n = len(arr)
        length = n - third
        if first + length <= second and second + length <= third:
            i = 0
            while third + i < n:
                if arr[first + i] != arr[second + i] or arr[first + i] != arr[third + i]:
                    return [-1, -1]
                i += 1
            return [first + length - 1, second + length]
        return [-1, -1]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/three-equal-parts/solution/san-deng-fen-by-leetcode-solution-3l2y/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。