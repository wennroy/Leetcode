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
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]