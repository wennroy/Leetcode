class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        record_set = set()
        for num in nums:
            record_set.add(num)
        max_len = 0
        # print(sorted(record_set))
        for i, num in enumerate(sorted(record_set)):
            if i == 0:
                prev = num
                start = 0
                continue
            if not num == prev + 1:
                if max_len < i - start:
                    max_len = i - start
                start = i
            prev = num
        if max_len < i - start + 1:
            max_len = i - start + 1
        return max_len

'''
执行用时：64 ms, 在所有 Python3 提交中击败了79.96%的用户
内存消耗：28.5 MB, 在所有 Python3 提交中击败了27.84%的用户
通过测试用例：
71 / 71
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

