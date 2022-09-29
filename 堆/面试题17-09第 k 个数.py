# 最小堆
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        import heapq
        min_heap = []
        heapq.heappush(min_heap, 1)
        last_ans, ans = -1, 0
        while k > 0:
            k -= 1
            ans = heapq.heappop(min_heap)
            if ans == last_ans:
                k += 1
                continue
            heapq.heappush(min_heap, ans * 3)
            heapq.heappush(min_heap, ans * 5)
            heapq.heappush(min_heap, ans * 7)
            last_ans = ans
        return ans

# 动态规划

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * (k + 1)
        dp[1] = 1
        p3 = p5 = p7 = 1

        for i in range(2, k + 1):
            num3, num5, num7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(num3, num5, num7)
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
            if dp[i] == num7:
                p7 += 1

        return dp[k]


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / get - kth - magic - number - lcci / solution / di - k - ge - shu - by - leetcode - solution - vzp7 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。