# 经典两数之和：利用二分查找来寻找答案

import bisect
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        idx_nums = sorted(list(range(n)), key=lambda x:nums[x])
        nums.sort()
        for i, num in enumerate(nums):
            j = bisect.bisect_left(nums[i+1:], target - num)+i+1
            if j <n and nums[j] == target-num:
                return [idx_nums[i],idx_nums[j]]

# 或者使用哈希表，经典做法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        record = defaultdict(int)
        for i, num in enumerate(nums):
            if target-num not in record.keys():
                record[num] = i
            else:
                return [record[target-num], i]