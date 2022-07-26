import math
import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        pattern = re.compile(r'(\+|-)?(\d+)/(\d+)')
        nums = [(-1 if x[0] == '-' else 1, int(x[1]),int(x[2])) for x in pattern.findall(expression)]

        # 新分母，也是约分前的结果分母
        bottom = math.lcm(*[x[2] for x in nums])
        # 新分子们
        ups = [x[0]*x[1]*(bottom//x[2]) for x in nums]

        # 结果分子
        up = sum(ups)

        # 约分
        gcd_ = math.gcd(up, bottom)
        up //= gcd_
        bottom //= gcd_

        # 结果
        return "".join([str(up),"/",str(bottom)])

# 作者：isuxiz
# 链接：https://leetcode.cn/problems/fraction-addition-and-subtraction/solution/by-isuxiz-ivyf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 标答
class Solution:
    def fractionAddition(self, expression: str) -> str:
        denominator, numerator = 0, 1  # 分子，分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子
            denominator1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1
            denominator1 = sign * denominator1
            i += 1

            # 读取分母
            numerator1 = 0
            while i < n and expression[i].isdigit():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1

            denominator = denominator * numerator1 + denominator1 * numerator
            numerator *= numerator1
        if denominator == 0:
            return "0/1"
        g = gcd(abs(denominator), numerator)
        return f"{denominator // g}/{numerator // g}"
