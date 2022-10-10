# 简单的异或和
# 异或和性质
from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        dp = [0] * n
        dp[0] = pref[0]
        for i in range(1, n):
            dp[i] = pref[i - 1] ^ pref[i]

        return dp