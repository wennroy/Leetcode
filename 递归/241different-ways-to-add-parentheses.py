# 分治法，外加记录递归
# 由于题目没说不能用eval，所以用eval简化流程
class Solution:
    def __init__(self):
        self.record = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.record.keys():
            return self.record[expression]

        pt = len(expression)
        ans = []
        number_flag = True
        while pt > 0:
            pt -= 1
            if expression[pt] == "+" or expression[pt] == "-" or expression[pt] == "*" or expression[pt] == "/":
                number_flag = False
                # print(expression)
                ans1 = self.diffWaysToCompute(expression[:pt])
                ans2 = self.diffWaysToCompute(expression[pt + 1:])
                for a in ans1:
                    for b in ans2:
                        ans.append(eval(str(a) + expression[pt] + str(b)))
                # print(ans)
        if number_flag:
            ans.append(int(expression))
        self.record[expression] = ans
        return ans
'''
官方解答一：记忆化搜索
基本与上面思路相同
'''


ADDITION = -1
SUBTRACTION = -2
MULTIPLICATION = -3

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = []
        i, n = 0, len(expression)
        while i < n:
            if expression[i].isdigit():
                x = 0
                while i < n and expression[i].isdigit():
                    x = x * 10 + int(expression[i])
                    i += 1
                ops.append(x)
            else:
                if expression[i] == '+':
                    ops.append(ADDITION)
                elif expression[i] == '-':
                    ops.append(SUBTRACTION)
                else:
                    ops.append(MULTIPLICATION)
                i += 1

        @cache
        def dfs(l: int, r: int) -> List[int]:
            if l == r:
                return [ops[l]]
            res = []
            for i in range(l, r, 2):
                left = dfs(l, i)
                right = dfs(i + 2, r)
                for x in left:
                    for y in right:
                        if ops[i + 1] == ADDITION:
                            res.append(x + y)
                        elif ops[i + 1] == SUBTRACTION:
                            res.append(x - y)
                        else:
                            res.append(x * y)
            return res
        return dfs(0, len(ops) - 1)

'''
官解二：动态规划
'''
ADDITION = -1
SUBTRACTION = -2
MULTIPLICATION = -3

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = []
        i, n = 0, len(expression)
        while i < n:
            if expression[i].isdigit():
                x = 0
                while i < n and expression[i].isdigit():
                    x = x * 10 + int(expression[i])
                    i += 1
                ops.append(x)
            else:
                if expression[i] == '+':
                    ops.append(ADDITION)
                elif expression[i] == '-':
                    ops.append(SUBTRACTION)
                else:
                    ops.append(MULTIPLICATION)
                i += 1

        n = len(ops)
        dp = [[[] for _ in range(n)] for _ in range(n)]
        for i, x in enumerate(ops):
            dp[i][i] = [x]
        for sz in range(3, n + 1):
            for r in range(sz - 1, n, 2):
                l = r - sz + 1
                for k in range(l + 1, r, 2):
                    for x in dp[l][k - 1]:
                        for y in dp[k + 1][r]:
                            if ops[k] == ADDITION:
                                dp[l][r].append(x + y)
                            elif ops[k] == SUBTRACTION:
                                dp[l][r].append(x - y)
                            else:
                                dp[l][r].append(x * y)
        return dp[0][-1]

'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/different-ways-to-add-parentheses/solution/wei-yun-suan-biao-da-shi-she-ji-you-xian-lyw6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
