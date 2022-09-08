# 直接按位数计算结果
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        bin_count = [0] * 32
        for num in nums:
            for k in range(32):
                bin_count[k] += (num >> k) & 1

        ans = 0
        for i in range(32):
            if bin_count[i] == 0:
                continue
            ans += bin_count[i] * (n - bin_count[i])

        return ans

# 可以不需要开辟新的数组
# sum内直接写for循环
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)   # 可以在sum内 for 循环
            ans += c * (n - c)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/total-hamming-distance/solution/yi-ming-ju-chi-zong-he-by-leetcode-solut-t0ev/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。