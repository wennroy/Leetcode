# 原地交换

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                if nums[nums[i]]== nums[i]:
                    return nums[i]
                else:
                    nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
        for i in range(len(nums)):
            if nums[i] != i:
                return nums[i]

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

# set
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1

# defaultdict
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        visited = defaultdict(int)
        for l in nums:
            if visited[l] > 0:
                return l
            visited[l] += 1

# list
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        visited = [0] * 10**6
        for l in nums:
            if visited[l] == 1:
                return l
            visited[l] += 1

# 超慢
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        visited = []
        for l in nums:
            if l in visited:
                return l
            visited.append(l)