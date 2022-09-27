# 动态规划

class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [[False, False]] * (n + 1)  # 第一位表示他是不是好数， 第二位表示他翻转完是否是个有效的数
        ans = 0
        set1 = set([0, 1, 2, 5, 6, 8, 9])
        set2 = set([2, 5, 6, 9])
        set3 = set([0, 1, 8])
        dp[0] = [False, True]
        for i in range(n + 1):
            str_i = str(i)
            first_digit = int(str_i[0])
            if i < 10:
                idx = 0
            else:
                idx = i % (first_digit * 10 ** (len(str_i) - 1))
            if dp[idx][1]:
                if dp[idx][0]:
                    if first_digit in set1:
                        ans += 1
                        dp[i] = [True, True]
                else:
                    if first_digit in set2:
                        ans += 1
                        dp[i] = [True, True]
                    elif first_digit in set3:
                        dp[i] = [False, True]
            # print(dp[i], i)
        return ans

# 数位动态规划
from functools import cache
class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        digits = [int(digit) for digit in str(n)]

        @cache
        def dfs(pos: int, bound: bool, diff: bool) -> int:
            if pos == len(digits):
                return int(diff)

            ret = 0
            for i in range(0, (digits[pos] if bound else 9) + 1):
                if check[i] != -1:
                    ret += dfs(
                        pos + 1,
                        bound and i == digits[pos],
                        diff or check[i] == 1
                    )

            return ret

        ans = dfs(0, True, False)
        dfs.cache_clear()
        return ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / rotated - digits / solution / xuan - zhuan - shu - zi - by - leetcode - solution - q9bh /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。