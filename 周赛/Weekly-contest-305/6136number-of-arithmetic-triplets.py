# 周赛的简单题，由于不小心误触了提交，多了五分钟
# nums.length最大值是200，所以直接暴力循环遍历即可
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        ans = 0
        for first in range(n - 2):
            second = first + 1
            while second < n - 2 and nums[second] < nums[first] + diff:
                second += 1
            if nums[second] != nums[first] + diff:
                continue
            third = second + 1
            while third < n - 1 and nums[third] < nums[second] + diff:
                third += 1
            if nums[third] == nums[second] + diff:
                ans += 1

        return ans