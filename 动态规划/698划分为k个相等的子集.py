from typing import List
from functools import cache
# 状态压缩+回溯
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_val = sum(nums)
        avg_val = sum_val / k
        n = len(nums)
        if sum_val % k:
            return False
        max_used = (1 << n) - 1

        @cache
        def dfs(used, val):
            if val == avg_val:
                val = 0

            if used == max_used:
                if val == 0:
                    return True
                else:
                    return False

            for i in range(n):
                if (used >> i) & 1 == 0 and val + nums[i] <= avg_val:
                    used |= (1 << i)
                    if dfs(used, val + nums[i]):
                        return True
                    used -= (1 << i)

            return False

        used = 0

        return dfs(used, 0)

# 状态压缩+记忆化搜索
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        all = sum(nums)
        if all % k:
            return False
        per = all // k
        nums.sort()  # 方便下面剪枝
        if nums[-1] > per:
            return False
        n = len(nums)

        @cache
        def dfs(s, p):
            if s == 0:
                return True
            for i in range(n):
                if nums[i] + p > per:
                    break
                if s >> i & 1 and dfs(s ^ (1 << i), (p + nums[i]) % per):  # p + nums[i] 等于 per 时置为 0
                    return True
            return False
        return dfs((1 << n) - 1, 0)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solution/hua-fen-wei-kge-xiang-deng-de-zi-ji-by-l-v66o/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 状压+动态规划
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        all = sum(nums)
        if all % k:
            return False
        per = all // k
        nums.sort()
        if nums[-1] > per:
            return False
        n = len(nums)
        dp = [False] * (1 << n)
        dp[0] = True
        cursum = [0] * (1 << n)
        for i in range(0, 1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if cursum[i] + nums[j] > per:
                    break
                if (i >> j & 1) == 0:
                    next = i | (1 << j)
                    if not dp[next]:
                        cursum[next] = (cursum[i] + nums[j]) % per
                        dp[next] = True
        return dp[(1 << n) - 1]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solution/hua-fen-wei-kge-xiang-deng-de-zi-ji-by-l-v66o/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 巧妙回溯
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        buckets = [sum(nums) // k] * k
        n = len(nums)
        nums.sort(reverse=True)
        ret = False
        def backTrack(i):
            nonlocal ret
            if i == n:
                ret = True
                return
            if ret:
                return
            seen = set()
            for b in range(k):
                if buckets[b] - nums[i] >= 0 and buckets[b] - nums[i] not in seen:
                    seen.add(buckets[b]-nums[i])
                    buckets[b] -= nums[i]
                    backTrack(i+1)
                    buckets[b]+= nums[i]
        backTrack(0)
        return ret