# 超时的字典树+栈
# 最坏的情况时间复杂度可能是O(n^n)
# 超时用例：
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 构建字典树
        tri = {}
        for word in wordDict:
            pt = tri
            for l in word:
                if l not in pt.keys():
                    pt[l] = {}
                pt = pt[l]
            if '#' not in pt.keys():
                pt['#'] = {}
        # 栈模拟递归
        n = len(s)
        stack = [0]
        while stack:
            i = stack.pop()
            if i >= n:
                continue
            pt = tri
            while pt and i < n:
                # print(i, s[i], pt.keys())
                if s[i] in pt.keys():
                    pt = pt[s[i]]
                    i += 1
                    if '#' in pt.keys():
                        if i == n:
                            return True
                        stack.append(i)
                else:
                    break
        return False


# 动态规划
# 时间复杂度O(n^2) 空间复杂度O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]


# 记忆化回溯
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)

# 作者：wu_yan_zu
# 链接：https://leetcode.cn/problems/word-break/solution/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
