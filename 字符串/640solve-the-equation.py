# 直接遍历求解，注意一下边界的判定
class Solution:
    def solveEquation(self, equation: str) -> str:
        left_eqn, right_eqn = equation.split('=')
        left_eqn += '+'
        right_eqn += '+'
        n1, n2 = len(left_eqn), len(right_eqn)
        x_coef = c_coef = 0

        i = 0
        if left_eqn[0] == '-':
            sign = -1
            i = 1
        else:
            sign = 1

        while i < n1:
            temp = ''
            while True:
                if left_eqn[i] == 'x':
                    x_coef += sign * int(temp) if temp else sign
                    i += 1
                    break
                elif left_eqn[i] == '+' or left_eqn[i] == '-':
                    c_coef += sign * int(temp)
                    break
                else:
                    temp += left_eqn[i]
                    i += 1
            sign = 1 if left_eqn[i] == '+' else -1
            i += 1

        i = 0
        if right_eqn[0] == '-':
            sign = 1
            i = 1
        else:
            sign = -1

        while i < n2:
            temp = ''
            while True:
                if right_eqn[i] == 'x':
                    x_coef += sign * int(temp) if temp else sign
                    i += 1
                    break
                elif right_eqn[i] == '+' or right_eqn[i] == '-':
                    c_coef += sign * int(temp)
                    break
                else:
                    temp += right_eqn[i]
                    i += 1
            sign = 1 if right_eqn[i] == '-' else -1
            i += 1
        if x_coef == 0 and c_coef == 0:
            return "Infinite solutions"
        elif x_coef == 0:
            return "No solution"
        else:
            return 'x=' + str(int(-c_coef / x_coef))


class Solution:
    def solveEquation(self, equation: str) -> str:
        factor = val = 0
        i, n, sign = 0, len(equation), 1  # 等式左边默认系数为正
        while i < n:
            if equation[i] == '=':
                sign = -1
                i += 1
                continue

            s = sign
            if equation[i] == '+':  # 去掉前面的符号
                i += 1
            elif equation[i] == '-':
                s = -s
                i += 1

            num, valid = 0, False
            while i < n and equation[i].isdigit():
                valid = True
                num = num * 10 + int(equation[i])
                i += 1

            if i < n and equation[i] == 'x':  # 变量
                factor += s * num if valid else s
                i += 1
            else:  # 数值
                val += s * num

        if factor == 0:
            return "No solution" if val else "Infinite solutions"
        return "No solution" if val % factor else f"x={-val // factor}"

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/solve-the-equation/solution/qiu-jie-fang-cheng-by-leetcode-solution-knct/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。