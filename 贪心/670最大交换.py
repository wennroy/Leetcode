# 时间复杂度O(n)，空间复杂度O(n)
# 贪心算法
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        num_list = list(map(int, str(num)))
        MinLeft = [0] * len(num_list)
        MinLeft[0] = num_list[0]
        max_val = idx = 0
        for i, val in enumerate(num_list[1:], 1):
            MinLeft[i] = min(MinLeft[i - 1], val)
            if val > MinLeft[i] and val >= max_val:
                max_val = val
                idx = i

        if idx:
            for i, val in enumerate(num_list):
                if max_val > val:
                    num_list[i], num_list[idx] = num_list[idx], num_list[i]
                    break
        ans = 0
        for i, val in enumerate(num_list[::-1]):
            ans += val * 10 ** i

        return ans

# 暴力遍历

class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        s = list(str(num))
        for i in range(len(s)):
            for j in range(i):
                s[i], s[j] = s[j], s[i]
                ans = max(ans, int(''.join(s)))
                s[i], s[j] = s[j], s[i]
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-swap/solution/zui-da-jiao-huan-by-leetcode-solution-lnd5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 贪心
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        maxIdx = n - 1
        idx1 = idx2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[maxIdx]:
                maxIdx = i
            elif s[i] < s[maxIdx]:
                idx1, idx2 = i, maxIdx
        if idx1 < 0:
            return num
        s[idx1], s[idx2] = s[idx2], s[idx1]
        return int(''.join(s))

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-swap/solution/zui-da-jiao-huan-by-leetcode-solution-lnd5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。