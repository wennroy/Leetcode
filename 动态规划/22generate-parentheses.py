# 自己写的动态规划，找到之前的结果，再拼接起来
# 唯一需要注意的是套多个'((( x )))'的情况，单独列出来放着。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = []
        dp.append(set(["()"]))
        for i in range(1,n):
            new_ans = set()
            for j in range(i):
                k = i - j - 1
                for s1 in dp[j]:
                    for s2 in dp[k]:
                        new_ans.add(s1+s2)
                        new_ans.add('('*(k+1) + s1 + ')'*(k+1))
            dp.append(new_ans)
        return list(dp[-1])


# 回溯法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 按括号序列的长度递归

class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

