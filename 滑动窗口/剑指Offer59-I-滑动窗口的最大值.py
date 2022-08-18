# 利用SortedDict来维护整个最大值
# 由于插入SortedDict需要时间复杂度O(logk)，总的时间复杂度为O(nlogk)
import heapq
from sortedcontainers import SortedDict
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cnt = SortedDict()
        n = len(nums)
        if n == k:
            return [max(nums)]
        for num in nums[:k]:
            if not num in cnt.keys():
                cnt[num] = 1
            else:
                cnt[num] += 1
        ans = []
        left, right = 0, k
        while right < n:
            ans.append(cnt.keys()[-1])
            if nums[right] not in cnt.keys():
                cnt[nums[right]] = 1
            else:
                cnt[nums[right]] += 1

            if cnt[nums[left]] == 1:
                cnt.pop(nums[left])
            else:
                cnt[nums[left]] -= 1
            left += 1
            right += 1
        ans.append(cnt.keys()[-1])

        return ans


# 优先队列
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
# 链接：https: // leetcode.cn / problems / hua - dong - chuang - kou - de - zui - da - zhi - lcof / solution / hua - dong - chuang - kou - de - zui - da - zhi - by - lee - ymyo /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 单调队列

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / hua - dong - chuang - kou - de - zui - da - zhi - lcof / solution / hua - dong - chuang - kou - de - zui - da - zhi - by - lee - ymyo /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 分块 + 预处理
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                prefixMax[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i + 1], nums[i])

        ans = [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/hua-dong-chuang-kou-de-zui-da-zhi-by-lee-ymyo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。