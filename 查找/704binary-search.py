# 超复杂binary search
# 注意Binary search 的范围
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l, r = 0, n - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            if r - l == 1:
                if nums[r] == target:
                    return r
                else:
                    return -1
            elif nums[mid] < target:
                l = mid
            else:
                r = mid

        return -1

# binary search 的下一个下标只可能出现在mid-1或者mid+1的位置，这样写可以保证在最后只剩
# 一个间隔的时候能够跳出while循环，而不需要另外的对于数组长度等的判断
'''
eg: left, right = 3, 4  mid = 3  nums = [0,1,2,3,5,6] target = 4

left = 3+1 = 4

right = 4 - 1 = 3 此时 3<4 跳出循环
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/binary-search/solution/er-fen-cha-zhao-by-leetcode-solution-f0xw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。