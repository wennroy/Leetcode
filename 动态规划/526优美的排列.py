# 由于n最大15，直接回溯即可
from collections import defaultdict
class Solution:
    def countArrangement(self, n: int) -> int:
        avalilable = defaultdict(set)
        if n <= 2:
            return n
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i % j == 0:
                    avalilable[i].add(j)
                    avalilable[j].add(i)

        ans = 0
        used = [False] * n

        def dfs(step, used):
            nonlocal ans
            if step == n:
                ans += 1
                return

            for nxt_num in avalilable[step + 1]:
                if not used[nxt_num - 1]:
                    used[nxt_num - 1] = True
                    dfs(step + 1, used)
                    used[nxt_num - 1] = False

            return

        dfs(0, used)
        return ans

# 和标答几乎一模一样
class Solution:
    def countArrangement(self, n: int) -> int:
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)

        num = 0
        vis = set()

        def backtrack(index: int) -> None:
            if index == n + 1:
                nonlocal num
                num += 1
                return

            for x in match[index]:
                if x not in vis:
                    vis.add(x)
                    backtrack(index + 1)
                    vis.discard(x)

        backtrack(1)
        return num


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / beautiful - arrangement / solution / you - mei - de - pai - lie - by - leetcode - solution - vea2 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 该回溯的时间复杂度为O(n!)，空间复杂度为O(n^2),拿来存储avaliable的结果。

# 朴素状压DP
class Solution:
    def countArrangement(self, n: int) -> int:
        mask = 1 << n
        dp = [[0] * mask for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for state in range(mask):
                # 枚举位置 i（最后一位）选的数值是 k
                for k in range(1,n+1):
                # 需要state的第k位没有被使用
                    if (state >> (k - 1)) & 1 == 0:
                        continue
                # 这个k满足要求
                    if k % i != 0 and i % k != 0:
                        continue
                    dp[i][state] += dp[i - 1][state & (~(1 << (k - 1)))]

        return dp[n][mask-1]


# 优化的状态压缩+DP
#
class Solution:
    def countArrangement(self, n: int) -> int:
        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1, 1 << n):
            num = bin(mask).count("1")
            for i in range(n):
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                    f[mask] += f[mask ^ (1 << i)]

        return f[(1 << n) - 1]


# 作者：LeetCode - Solution
# 链接：https://leetcode.cn/problems/beautiful-arrangement/solution/you-mei-de-pai-lie-by-leetcode-solution-vea2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    sol = Solution()
    print(sol.countArrangement(15))
