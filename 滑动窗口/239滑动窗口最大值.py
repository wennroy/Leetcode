from sortedcontainers import SortedDict
import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        cnt = SortedDict()
        for i in range(k):
            cnt[nums[i]] = cnt.setdefault(nums[i], 0) + 1
        ans[0] = cnt.keys()[-1]
        for i in range(n - k):
            cnt[nums[i]] -= 1
            cnt[nums[i + k]] = cnt.setdefault(nums[i + k], 0) + 1
            if cnt[nums[i]] == 0:
                cnt.pop(nums[i])

            ans[i + 1] = cnt.keys()[-1]

        return ans


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / sliding - window - maximum / solution / hua - dong - chuang - kou - zui - da - zhi - by - leetco - ki6m /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
