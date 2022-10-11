# 有点意思的单调栈
# 额外腾出空间来解决循环问题
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        nums += nums
        ans = [-1] * n
        flag = False
        for i, val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                idx = stack.pop()
                if stack and stack[0] >= n:
                    flag = True
                    break
                if idx < n:
                    ans[idx] = val
            if flag:
                break
            stack.append(i)

        return ans

# 利用i%N解决循环问题
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[stack[-1]] < nums[i % N]:
                res[stack.pop()] = nums[i % N]
            stack.append(i % N)
        return res

# 作者：fuxuemingzhu
# 链接：https://leetcode.cn/problems/next-greater-element-ii/solution/dong-hua-jiang-jie-dan-diao-zhan-by-fuxu-4z2g/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。