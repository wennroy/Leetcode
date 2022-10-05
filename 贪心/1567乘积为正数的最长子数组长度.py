# 什么都可以贪！贪就完事了
# 情况需要考虑全
from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        last_neg = -1
        first_neg = -1
        for i, num in enumerate(nums):
            if num == 0:
                cur = 0
                last_neg = -1
                first_neg = -1
            else:
                cur += 1
                if num < 0:
                    if first_neg == -1:
                        first_neg = i
                    if last_neg == -1:
                        last_neg = i
                        ans = max(ans, cur-1)
                    else:
                        ans = max(ans, cur)
                        last_neg = -1
                else:
                    if last_neg == -1:
                        ans = max(ans, cur)
                    else:
                        ans = max(i-first_neg, ans)
        return ans

# 利用列表记录
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        neg_ind = []
        zero_ind = -1
        res = 0
        for i, num in enumerate(nums):
            if num < 0:
                neg_ind.append(i)
            elif num == 0:
                neg_ind, zero_ind = [], i
            if len(neg_ind) % 2 == 0:
                res = max(res, i - zero_ind)
            else:
                res = max(res, i - neg_ind[0])
        return res