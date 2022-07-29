# 经典面试双指针

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# 由于水的容量是由较小的那一侧决定的，那么我们只要保持最大的一侧不动，就能遍历所有可能更大的情况。当我们只移动最短的那侧时，
# 我们能保证被排除掉的情况都是比当前情况来得小的，因此保证了算法的安全性。