# 前缀和+哈希表
from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        psum = [0] * (n + 1)
        psum[0] = 0
        for i in range(1, n + 1):
            psum[i] = psum[i - 1] + nums[i - 1]

        # 哈希表
        ans = 0
        record = dict()
        for i in range(n + 1):
            if psum[i] + k not in record.keys():
                record[psum[i] + k] = i
            if psum[i] in record.keys():
                ans = max(ans, i - record[psum[i]])
        # print(record)
        return ans

# 只用了一个pre来存储，节省了O(n)的存储空间。
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dct = dict()
        n = len(nums)
        pre = 0
        dct[0] = -1
        ans = 0
        for i in range(n):
            pre += nums[i]
            if pre - k in dct and i - dct[pre - k] > ans:
                ans = i - dct[pre - k]
            if pre not in dct:
                dct[pre] = i
        return ans

# 作者：liupengsay
# 链接：https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/solution/-by-liupengsay-w0wh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。