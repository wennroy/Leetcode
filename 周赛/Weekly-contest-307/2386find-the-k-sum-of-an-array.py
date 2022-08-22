class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        import heapq
        tot_sum = 0
        for i, num in enumerate(nums):
            if num >= 0: tot_sum += num
            else: nums[i] = -num
        # 最大的子序列和 - (第k-1小的子序列和)即为答案
        # 第k-1小的子序列和，
        nums.sort()
        print(nums)
        h = [(0, 0)]
        while k > 1:
            print(h)
            k -= 1
            sub_sum, i = heapq.heappop(h)
            if i < len(nums):
                heapq.heappush(h, (sub_sum + nums[i], i+1))
                if i: heapq.heappush(h, (sub_sum + nums[i] - nums[i-1], i+1))

        return tot_sum - h[0][0]

if __name__ == '__main__':
    sol = Solution()
    nums = [2,4,-2]
    k = 6
    print(sol.kSum(nums, k))