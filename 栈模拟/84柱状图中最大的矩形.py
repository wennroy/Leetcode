# 看到提示单调栈瞬间就会了
# 服了

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 维护一个最小单调栈
        stack = []  # (最大能向左延伸到第i位，的最大值)
        max_area = 0
        n = len(heights)
        for i, val in enumerate(heights):
            left_idx = i
            while stack and val <= stack[-1][1]:
                idx, min_val = stack.pop()
                cur_area = (i - idx) * min_val
                max_area = max(max_area, cur_area)
                left_idx = min(left_idx, idx)
            stack.append((left_idx, val))

        for i, val in stack:
            cur_area = (n - i) * val
            max_area = max(max_area, cur_area)

        return max_area
