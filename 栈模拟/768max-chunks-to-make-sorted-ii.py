# 硬解
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        sort_arr = sorted(arr)
        left = right = 0
        stack = []
        ans = 0
        while right < n:
            m = arr[right]
            if not stack or m == stack[-1]:
                stack.append(m)
            elif m > stack[-1]:
                stack = [m]

            stack_len = len(stack)
            last = stack[-1]
            l = stack_len-1
            while l>=0 and last == stack[l]:
                l -= 1
            min_ind = left + bisect.bisect_left(sort_arr[left:], last) + (stack_len - l - 2)
            if min_ind == right:
                ans += 1
                stack = []
                left = right + 1
            right += 1

        return ans

# 方法一：排序+哈希表
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = Counter()
        res = 0
        for x, y in zip(arr, sorted(arr)):
            cnt[x] += 1
            if cnt[x] == 0:
                del cnt[x]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            if len(cnt) == 0:
                res += 1
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-ii-w5c6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法二：单调栈
class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        stack = []
        for a in arr:
            if len(stack) == 0 or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                while stack and stack[-1] > a:
                    stack.pop()
                stack.append(mx)
        return len(stack)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-ii-w5c6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。