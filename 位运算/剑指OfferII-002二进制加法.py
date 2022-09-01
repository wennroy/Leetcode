class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
            print(x,y)
        return bin(x)[2:]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/JFETK5/solution/er-jin-zhi-jia-fa-by-leetcode-solution-fa6t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。