# 懒得思考，硬解
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        digits = [0, 0, 0, 0]
        for i in range(3, -1, -1):
            digits[i] = num % 10
            num //= 10
        ans += 'M' * digits[0]
        # 百位
        if digits[1] == 9:
            ans += 'CM'
            digits[1] -= 9

        elif digits[1] == 4:
            ans += 'CD'
            digits[1] -= 4

        elif digits[1] >= 5:
            ans += 'D'
            digits[1] -= 5

        ans += 'C' * digits[1]
        # 十位
        if digits[2] == 9:
            ans += 'XC'
            digits[2] -= 9

        elif digits[2] == 4:
            ans += 'XL'
            digits[2] -= 4

        elif digits[2] >= 5:
            ans += 'L'
            digits[2] -= 5

        ans += 'X' * digits[2]
        # 个位
        if digits[3] == 9:
            ans += 'IX'
            digits[3] -= 9

        elif digits[3] == 4:
            ans += 'IV'
            digits[3] -= 4

        elif digits[3] >= 5:
            ans += 'V'
            digits[3] -= 5

        ans += 'I' * digits[3]

        return ans


# 贪心一下
class Solution:

    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def intToRoman(self, num: int) -> str:
        roman = list()
        for value, symbol in Solution.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcod-75rs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。