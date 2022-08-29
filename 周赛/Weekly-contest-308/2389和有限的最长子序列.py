# 简单题写了20分钟，很不应该
# 排序+贪心即可

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        m = len(queries)
        n = len(nums)
        ans = [0] * m
        sorted_id = sorted(range(m), key=lambda x: queries[x])
        sub_sum = sum(nums)
        k = n
        i = m - 1
        while i >= 0 and k >= 1:
            while i >= 0 and sub_sum <= queries[sorted_id[i]]:
                ans[sorted_id[i]] = k
                i -= 1
            k -= 1
            sub_sum -= nums[k]
        return ans

# 贪心+二分+前缀和
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]  # 原地求前缀和
        for i, q in enumerate(queries):
            queries[i] = bisect_right(nums, q)  # 复用 queries 作为答案
        return queries

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-subsequence-with-limited-sum/solution/fei-bao-li-zuo-fa-qian-zhui-he-er-fen-by-ny4m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。