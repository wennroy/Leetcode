# 直接暴力二分查找
# 第一次莫名其妙24ms，击败99.5%xs
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        if not nums or target < nums[0] or target > nums[-1]:
            return 0
        idx = bisect_left(nums, target)
        n = len(nums)
        ans = 0
        while idx < n and target == nums[idx]:
            ans += 1
            idx += 1
        return ans

# 手写二分，寻找左边界与右边界

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def bisearch(nums: list[int], target: int, lower: bool) -> int:
            l, r = 0, n-1
            ans = n
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target or (lower and nums[mid] >= target):
                    r = mid -1
                    ans = mid
                else:
                    l = mid + 1

            return ans

        n = len(nums)
        leftIdx = bisearch(nums, target, True)
        rightIdx = bisearch(nums, target, True)
        if leftIdx <= rightIdx < n and nums[leftIdx] == target and nums[rightIdx] == target:
            return rightIdx - leftIdx + 1
        return 0


'''
class Solution {
    public int search(int[] nums, int target) {
        int leftIdx = binarySearch(nums, target, true);
        int rightIdx = binarySearch(nums, target, false) - 1;
        if (leftIdx <= rightIdx && rightIdx < nums.length && nums[leftIdx] == target && nums[rightIdx] == target) {
            return rightIdx - leftIdx + 1;
        } 
        return 0;
    }

    public int binarySearch(int[] nums, int target, boolean lower) {
        int left = 0, right = nums.length - 1, ans = nums.length;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] > target || (lower && nums[mid] >= target)) {
                right = mid - 1;
                ans = mid;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
}

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-wl6kr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''