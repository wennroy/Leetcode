class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
                "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM": 900}
        n = len(s)
        pt = 0
        while pt < n:
            if s[pt:(pt+2)] in value.keys():
                ans += value[s[pt:(pt+2)]]
                pt += 2
            else:
                ans += value[s[pt]]
                pt += 1
        return ans


class Solution:

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans
'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/roman-to-integer/solution/luo-ma-shu-zi-zhuan-zheng-shu-by-leetcod-w55p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
