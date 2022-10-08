# 直接计算总和
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = []
        n = len(s)
        i = 0
        depth = 0
        while i < n:
            while i < n and s[i] == '(':
                depth += 1
                i += 1
            cnt = 0
            while i < n and s[i] == ')':
                cnt += 1
                i += 1
            while len(ans) < depth:
                ans.append(0)
            ans[depth-1] += 1
            # print(ans, depth, cnt)
            for j in range(depth-1, depth-cnt, -1):
                ans[j-1] += ans[j] * 2
                ans[j] = 0
            # print(ans)
            depth = depth - cnt
        return ans[0]

# 标答的分治
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        if n == 2:
            return 1
        bal = 0
        for i, c in enumerate(s):
            bal += 1 if c == '(' else -1
            if bal == 0:
                if i == n - 1:
                    return 2 * self.scoreOfParentheses(s[1:-1])
                return self.scoreOfParentheses(s[:i + 1]) + self.scoreOfParentheses(s[i + 1:])

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/score-of-parentheses/solution/gua-hao-de-fen-shu-by-leetcode-solution-we6b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 栈模拟
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += max(2 * v, 1)
        return st[-1]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/score-of-parentheses/solution/gua-hao-de-fen-shu-by-leetcode-solution-we6b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 计算最终得分和
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = bal = 0
        for i, c in enumerate(s):
            bal += 1 if c == '(' else -1
            if c == ')' and s[i - 1] == '(':
                ans += 1 << bal
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/score-of-parentheses/solution/gua-hao-de-fen-shu-by-leetcode-solution-we6b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。