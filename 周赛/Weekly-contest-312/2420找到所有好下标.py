# https://leetcode.cn/problems/find-all-good-indices/
# 两次dp找到左右两侧的下降上升数目
# 再遍历一次即可

from typing import List
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        dp_up = [1] * n
        dp_down = [1] * n

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                dp_down[i] = dp_down[i - 1] + 1
            else:
                dp_down[i] = 1

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                dp_up[i] = dp_up[i + 1] + 1
            else:
                dp_up[i] = 1
        # print(dp_up)
        # print(dp_down)
        ans = []
        for i in range(1, n - 1):
            if dp_up[i + 1] >= k and dp_down[i - 1] >= k:
                ans.append(i)

        return ans