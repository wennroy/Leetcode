# 二分查找+双指针，时间复杂度O(logn + k)，空间复杂度O(k)，腾出了k的空间存储答案

import bisect
from collections import deque


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        n = len(arr)
        if idx == 0:
            return arr[:k]

        ans = deque()
        left = idx - 1
        right = idx

        while k > 0 and left >= 0 and right <= n - 1:
            k -= 1
            # print(ans, arr[left], arr[right])
            if x - arr[left] <= arr[right] - x:
                ans.appendleft(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1

        if left < 0 and k > 0:
            return list(ans) + arr[right:right + k]
        if right > n - 1 and k > 0:
            return arr[left - k + 1:left + 1] + list(ans)

        return list(ans)

# 直接暴力排序
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v: abs(v - x))
        return sorted(arr[:k])

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/find-k-closest-elements/solution/zhao-dao-k-ge-zui-jie-jin-de-yuan-su-by-ekwtd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 标答空间复杂度为O(1)的答案
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect.bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/find-k-closest-elements/solution/zhao-dao-k-ge-zui-jie-jin-de-yuan-su-by-ekwtd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。