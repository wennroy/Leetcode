# 直接排序
# 时间复杂度 O(nlogn)
# 空间复杂度 O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        res = Counter(nums).most_common(k)
        ans = []
        for i, _ in res:
            ans.append(i)

        return ans

# 利用python的堆排序

'''
作者：edelweisskoko
链接：https://leetcode.cn/problems/top-k-frequent-elements/solution/347-qian-k-ge-gao-pin-yuan-su-zhi-jie-pa-wemd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = [(val, key) for key, val in count.items()]
        return [item[1] for item in heapq.nlargest(k, heap)]

'''
复杂度分析
时间复杂度：O(nlogn)，主要在nlargest这里，至于是不是nlogn不太清楚，也可能是nlogk？
空间复杂度：O(n)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        for key, val in count.items():
            if len(heap) >= k:
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        return [item[1] for item in heap]
