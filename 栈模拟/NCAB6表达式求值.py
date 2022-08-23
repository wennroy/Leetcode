# 经典的表达式求和，字符串转后缀表达式

# https://www.nowcoder.com/practice/c215ba61c8b1443b996351df929dc4d4
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
class Solution:
    def solve(self, s):
        """后缀表达式求值"""

        suffix = self.infix_to_suffix(s)
        stack = []
        for item in suffix:
            if item not in ["+", "-", "*"]:
                stack.append(int(item))
            else:
                a, b = stack.pop(), stack.pop()
                if item == "+":
                    stack.append(a + b)
                elif item == "-":
                    stack.append(b - a)
                elif item == "*":
                    stack.append(a * b)
        return stack.pop()

    def priority(self, op):
        """操作符的优先级"""

        if op == "*":
            return 1
        elif op == "+" or op == "-":
            return 0
        else:
            return -1

    def infix_to_suffix(self, s):
        """中缀表达式转后缀表达式"""

        # 后缀表达式结果
        res = []
        # 操作符栈
        stack = []
        num = ""
        for c in s:
            # 多位操作数以字符串形式记录
            if c.isdigit():
                num += c
            else:
                # 遍历到操作符，将前面记录的操作数直接加入后缀表达式
                if num != "":
                    res.append(num)
                num = ""
                if c in ["+", "-", "*"]:
                    # 如果栈不空，且新来的操作符优先级比栈顶低，就出栈加入后缀表达式
                    while len(stack) != 0 and self.priority(c) <= self.priority(stack[-1]):
                        res.append(stack.pop())
                    # 新操作符进栈
                    stack.append(c)
                elif c == "(":
                    stack.append(c)
                elif c == ")":
                    while stack[-1] != "(":
                        res.append(stack.pop())
                    stack.pop()
        # 最后一个操作数后面没有操作符，额外处理
        if num != "":
            res.append(num)
        while len(stack) != 0:
            res.append(stack.pop())
        return res