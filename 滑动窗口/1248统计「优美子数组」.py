# 滑动窗口，计算乘积
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_num = []
        for i, val in enumerate(nums):
            if val % 2 == 1:
                odd_num.append(i)

        left, right = 0, 0
        n = len(odd_num)
        if n < k:
            return 0
        while right < n and right - left < k:
            right += 1

        ans = 0
        while right < n:
            if left:
                ans += (odd_num[left] - odd_num[left - 1]) * (odd_num[right] - odd_num[right - 1])
            else:
                ans += (odd_num[left] + 1) * (odd_num[right] - odd_num[right - 1])
            left += 1
            right += 1

        if left:
            ans += (odd_num[left] - odd_num[left - 1]) * (len(nums) - odd_num[-1])
        else:
            ans += (odd_num[left] + 1) * (len(nums) - odd_num[-1])
        return ans

# 注意边界处理

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/count-number-of-nice-subarrays/solution/tong-ji-you-mei-zi-shu-zu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。