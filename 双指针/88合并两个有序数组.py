# 简单双指针

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 双指针
        if n == 0:
            return None
        if m == 0:
            for i, val in enumerate(nums2):
                nums1[i] = val
            return None
        pt1, pt2 = m - 1, n - 1
        pt = m + n - 1
        while pt >= 0 and pt1 >= 0 and pt2 >= 0:
            if nums1[pt1] <= nums2[pt2]:
                nums1[pt] = nums2[pt2]
                pt2 -= 1
            else:
                nums1[pt] = nums1[pt1]
                pt1 -= 1
            pt -= 1

        if pt2 >= 0:
            nums1[:pt2 + 1] = nums2[:pt2 + 1]
        return None