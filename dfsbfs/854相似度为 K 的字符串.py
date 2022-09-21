# 标答BFS
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        step, n = 0, len(s1)
        q, vis = [(s1, 0)], {s1}
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in vis:
                            vis.add(t)
                            q.append((t, i + 1))
            step += 1

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/k-similar-strings/solution/xiang-si-du-wei-k-de-zi-fu-chuan-by-leet-8z10/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 重复遍历好几遍前面的数字，导致最终超时

from collections import defaultdict

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        record = defaultdict(lambda :False)
        record[s1] = True
        if s1 == s2:
            return 0
        n = len(s1)

        idx_record = defaultdict(list)
        for i, val in enumerate(s2):
            idx_record[val].append(i)
        nxt_strings = set([s1])
        ans = 0
        while s2 not in nxt_strings:
            cur_strings = nxt_strings
            nxt_strings = set()
            for s in cur_strings:
                i = 0
                while i < n and s[i] == s2[i]:
                    i += 1
                    for idx in idx_record[s[i]]:
                        if idx > i and s2[idx] != s[idx]:
                            nxt_s = list(s)
                            nxt_s[idx], nxt_s[i] = nxt_s[i], nxt_s[idx]
                            nxt_s = ''.join(nxt_s)
                            if record[nxt_s] == False:
                                nxt_strings.add(nxt_s)
                                record[nxt_s] = True
            if ans >= 5:
                print(nxt_strings)
            ans += 1
        return ans

# BFS
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        step, n = 0, len(s1)
        q, vis = [(s1, 0)], {s1}
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in vis:
                            vis.add(t)
                            q.append((t, i + 1))
            step += 1

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/k-similar-strings/solution/xiang-si-du-wei-k-de-zi-fu-chuan-by-leet-8z10/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# DFS

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        s, t = [], []
        for x, y in zip(s1, s2):
            if x != y:
                s.append(x)
                t.append(y)
        n = len(s)
        if n == 0:
            return 0

        ans = n - 1
        def dfs(i: int, cost: int) -> None:
            nonlocal ans
            if cost > ans:
                return
            while i < n and s[i] == t[i]:
                i += 1
            if i == n:
                ans = min(ans, cost)
                return
            diff = sum(s[j] != t[j] for j in range(i, len(s)))
            min_swap = (diff + 1) // 2
            if cost + min_swap >= ans:  # 当前状态的交换次数下限大于等于当前的最小交换次数
                return
            for j in range(i + 1, n):
                if s[j] == t[i]:
                    s[i], s[j] = s[j], s[i]
                    dfs(i + 1, cost + 1)
                    s[i], s[j] = s[j], s[i]
        dfs(0, 0)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/k-similar-strings/solution/xiang-si-du-wei-k-de-zi-fu-chuan-by-leet-8z10/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    s1 = "cdebcdeadedaaaebfbcf"
    s2 = "baaddacfedebefdabecc"
    sol = Solution()
    print(sol.kSimilarity(s1, s2))