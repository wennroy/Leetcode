# 排序之后快速合并区间
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = []
        start = end = -1
        for interval in intervals:
            if interval[0] > end:
                ans.append([start, end])
                start = interval[0]
                end = interval[1]
            else:
                end = max(end, interval[1])

        ans.append([start, end])
        ans.pop(0)
        return ans