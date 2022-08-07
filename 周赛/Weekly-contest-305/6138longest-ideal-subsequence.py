# 一定要记得从值域的方向出发。直接对数组dp的话，转移方程需再遍历前面的所有结果，导致时间复杂度O(n^2)超时
# 利用值域的26个取值来解答，最终计算dp中的最大值。

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26
        for i, val in enumerate(s):
            temp = 0
            for j in range(26):
                if abs(ord(val) - (j+ord('a'))) <= k:
                    temp = max(temp, dp[j] + 1)
            dp[ord(val)-ord('a')] = temp
        return max(dp)