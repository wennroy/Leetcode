# 贪心就完事了
from typing import List
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        mapped_num2 = sorted(range(n), key=lambda x:nums2[x])
        nums1.sort()
        i = 0
        ans = [0] * n
        right = n-1
        for j in range(n):
            while i < n and nums1[i] <= nums2[mapped_num2[j]]:
                ans[mapped_num2[right]] = nums1[i]
                right -= 1
                i += 1
            if i == n:
                break
            ans[mapped_num2[j]] = nums1[i]
            i += 1
        return ans


# 标答的贪心
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        idx1, idx2 = list(range(n)), list(range(n))
        idx1.sort(key=lambda x: nums1[x])
        idx2.sort(key=lambda x: nums2[x])

        ans = [0] * n
        left, right = 0, n - 1
        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[left]]:
                ans[idx2[left]] = nums1[idx1[i]]
                left += 1
            else:
                ans[idx2[right]] = nums1[idx1[i]]
                right -= 1

        return ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / advantage - shuffle / solution / you - shi - xi - pai - by - leetcode - solution - sqsf /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。