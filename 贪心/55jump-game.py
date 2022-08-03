# 最坏的情况为O(n2)，超时
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n-2, -1, -1):
            for j in range(nums[i]):
                if i+j+1<n and dp[i+j+1]:
                    dp[i] = True
                    break
        return dp[0]


# 究极暴力解法，直接上lru_cache，扩大递归深度。
# 7792ms + 54.2MB
from functools import lru_cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def canJump_start(i):
            if i == n-1:
                return True
            for k in range(1, nums[i]+1):
                if canJump_start(i+k):
                    return True
            return False
        return canJump_start(0)

# 贪心算法1，寻找能够探测最远的index，适用于45jump-game-ii
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i<n-1:
            max_step = 0
            nxt_move = 0
            for k in range(1,nums[i]+1):
                if i+k < n and max_step <= nums[i+k] + k:
                    nxt_move, max_step= k, k + nums[i+k]
            if nxt_move == 0:
                return False
            i += nxt_move
        return True

# 标答贪心算法2：对每个点进行遍历，查看他们最远能到哪。实时维护 最远可以到达的位置
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

# 标答基础上改进贪心算法3：当发现i >rightmost的时候 ，说明之前的rightmost已经够不到i了，此时返回False
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
            else:
                return False
        return False

