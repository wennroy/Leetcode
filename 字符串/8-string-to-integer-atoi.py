INT_MAX = 2**31
INT_RANGE = [-INT_MAX, INT_MAX - 1]
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        n = len(s)
        if not s:
            return 0
        i = 0
        if not ord('0') <= ord(s[i]) <= ord('9'):
            return 0
        while i<n and ord('0') <= ord(s[i]) <= ord('9'):
            i += 1
        ans = sign * int(s[:i])
        if ans <INT_RANGE[0]:
            return INT_RANGE[0]
        elif ans > INT_RANGE[1]:
            return INT_RANGE[1]
        else:
            return ans

# 字符串处理的题目往往涉及复杂的流程以及条件情况，如果直接上手写程序，一不小心就会写出极其臃肿的代码。
# 说的就是我

# 标答自动机的写法

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / string - to - integer - atoi / solution / zi - fu - chuan - zhuan - huan - zheng - shu - atoi - by - leetcode - /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。