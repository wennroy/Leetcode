# 标答：贪心+优先队列
from math import inf
from heapq import heappush, heappop
from typing import List
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
        ans = inf
        totalq = 0
        h = []
        # 维护一个大根堆
        for q, w in pairs[:k - 1]:
            totalq += q
            heappush(h, -q)
        # 遍历一遍之后，我们选quality尽量少的组合
        for q, w in pairs[k - 1:]:
            totalq += q
            heappush(h, -q)
            ans = min(ans, w / q * totalq)
            totalq += heappop(h)
        return ans

