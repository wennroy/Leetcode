# k=0选用哈希表，k不等于0选用 自由 双指针
from collections import *

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            record = defaultdict(int)
            for val in nums:
                record[val] += 1
            ans = 0
            for val in record.values():
                if not val == 1:
                    ans += 1
            return ans
        nums = list(set(nums))
        nums.sort()
        left, right = 0, 1
        n = len(nums)
        ans = 0
        while right < n:
            diff_val = nums[right] - nums[left]
            if diff_val < k:
                right += 1
            elif diff_val > k:
                left += 1
            else:
                ans += 1
                if right == n-1:
                    break
                else:
                    if nums[right + 1] - nums[right] >= nums[left+1] - nums[left]:
                        left += 1
                    else:
                        right += 1
        return ans

'''
标答 哈希表
直接利用哈希表遍历一遍
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited, res = set(), set()
        for num in nums:
            if num - k in visited:
                res.add(num - k)
            if num + k in visited:
                res.add(num)
            visited.add(num)
        return len(res)

'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/k-diff-pairs-in-an-array/solution/shu-zu-zhong-de-k-diff-shu-dui-by-leetco-ane6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, y, res = len(nums), 0, 0
        for x in range(n):
            if x == 0 or nums[x] != nums[x - 1]:
                while y < n and (nums[y] < nums[x] + k or y <= x):
                    y += 1
                if y < n and nums[y] == nums[x] + k:
                    res += 1
        return res

'''
双指针

相较于我的方法，标答先固定左指针，然后移动右指针寻找合适的值，找到了就停。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/k-diff-pairs-in-an-array/solution/shu-zu-zhong-de-k-diff-shu-dui-by-leetco-ane6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''