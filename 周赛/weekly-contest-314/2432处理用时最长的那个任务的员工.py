# 增加参与感的题目
from typing import List
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        logs.sort(key=lambda x:x[1])
        last = 0
        max_time = 0
        ans = 6000
        for log in logs:
            cur_time = log[1] - last
            if cur_time > max_time:
                max_time = cur_time
                ans = log[0]
            elif cur_time == max_time:
                ans = min(ans, log[0])
            last = log[1]
        return ans