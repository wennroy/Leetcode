# 双指针的解法 - 题解中属于快慢双指针

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, 1
        n = len(nums)
        if n <= 1:
            return nums

        if nums[left] % 2 == 0:
            while right < n:
                if nums[right] % 2 == 1:
                    break
                right += 1
            if right == n:
                return nums
            nums[left], nums[right] = nums[right], nums[left]

        while right < n:
            if nums[right] % 2 == 1:
                nums[left + 1], nums[right] = nums[right], nums[left + 1]
                left += 1
            right += 1

        return nums

# 头尾双指针
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

# 作者：jyd
# 链接：https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/mian-shi-ti-21-diao-zheng-shu-zu-shun-xu-shi-qi-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 暴力开空间存储数据

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd_list, even_list = [], []
        for num in nums:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
        return odd_list + even_list