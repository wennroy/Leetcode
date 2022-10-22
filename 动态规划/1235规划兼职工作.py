# 感觉是一道不是很难的困难 动态规划，但居然没想清楚
# dp[i]=max(dp[i−1],dp[k]+profit[i−1])
from bisect import bisect_right
from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda p: p[1])
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            k = bisect_right(jobs, jobs[i - 1][0], hi=i, key=lambda p: p[1])
            dp[i] = max(dp[i - 1], dp[k] + jobs[i - 1][2])
        return dp[n]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solution/gui-hua-jian-zhi-gong-zuo-by-leetcode-so-gu0e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # 如果用startTime sort的话
        jobs = sorted(zip(startTime, endTime, profit), key=lambda p: p[0])
        dp = [0] * (n + 1)
        # 那么需要考虑所有在endTime后面的starTime
        # 也就是k表示满足startTime大于等于第i份工作结束时间的编号。
        for i in range(n-1, -1, -1):
            k = bisect_left(jobs, jobs[i][1], lo=i, key=lambda p:p[0])
            dp[i] = max(dp[i+1], dp[k] + jobs[i][2])
        return dp[0]