# 单调栈实现
from collections import defaultdict
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 1. 单调栈，找到在什么区域内，这个数字是最小的
        # 2. 直接遍历，计算多少个子数组包含这个数字

        # 单调栈实现
        n = len(arr)
        stack = []  # (val, index, val_idx)
        min_range = defaultdict(list)
        for i, val in enumerate(arr):
            left_idx = i
            while stack:
                cur_val, cur_idx, val_idx = stack.pop()
                if val < cur_val:   # 这里取等于和不取等于结果是一致的。2*3+5*5 和 5*2+7*3都为31。中间那一段只有一边会进行计算。
                    min_range[cur_val].append((cur_idx, val_idx, i))
                    left_idx = cur_idx
                else:
                    stack.append((cur_val, cur_idx, val_idx))
                    break
            stack.append((val, left_idx, i))
        while stack:
            cur_val, cur_idx, val_idx = stack.pop()
            min_range[cur_val].append((cur_idx, val_idx, n))

        # print(min_range)
        # 直接遍历
        ans = 0
        for val in min_range.keys():
            for left, val_idx, right in min_range[val]:
                ans += val * (val_idx - left + 1) * (right - val_idx)

        return ans % (10 ** 9 + 7)


# 开辟两个数组来计算最左侧的最小值和最右侧的最小值，方便理解。
class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_A = len(A)
        if len_A == 0:
            return 0
        if len_A == 1:
            return A[0]

        ans = 0
        left = [0] * len_A
        right = [0] * len_A

        stack = []
        for i in range(len_A):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(len_A - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if not stack:
                right[i] = len_A
            else:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(len_A):
            ans += (i - left[i]) * (right[i] - i) * A[i]
            ans %= 1000000007
        return ans


# 作者：smoon1989
# 链接：https: // leetcode.cn / problems / sum - of - subarray - minimums / solution / dan - diao - zhan - python3 - by - smoon1989 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        A = [float('-inf')] + A + [float('-inf')]
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                ans += A[cur] * (i-cur) * (cur-stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)

# 作者：smoon1989
# 链接：https://leetcode.cn/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-python3-by-smoon1989/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。