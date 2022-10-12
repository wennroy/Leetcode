# 贪心，维护一个sorted的数组，利用bisect模块的insort维护。
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        import bisect
        ans = 0
        n = len(arr)
        L = []
        right = 0
        while right < n:
            bisect.insort(L, arr[right])
            if L[-1] == right:
                ans += 1
            right += 1
        return ans

# 标答方法：暴力。说是暴力，但其实也不暴力
class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans

# 作者：LeetCode
# 链接：https://leetcode.cn/problems/max-chunks-to-make-sorted/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-i-by-leetcod/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 单调栈，维护一个最后一位永远是最大值得单调栈
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        stack=[]
        for i in range(n):
            m = arr[i]
            while stack and stack[-1] > arr[i]:
                m = max(stack.pop(), m)
            stack.append(m)
        return len(stack)

# 作者：20185944
# 链接：https://leetcode.cn/problems/max-chunks-to-make-sorted/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-by-d1nt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 1012/2022更新
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        idx_list = sorted(range(n), key=lambda x: arr[x])
        ans = 0
        cur_block = 0
        for i in range(n):
            if i == cur_block and idx_list[i] <= cur_block:
                ans += 1
                cur_block += 1
            else:
                cur_block = max(cur_block, idx_list[i])

        return ans
