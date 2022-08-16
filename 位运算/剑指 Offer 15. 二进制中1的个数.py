# 直接丑陋写法了
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 0:
            n = bin(n)[3:]
        else:
            n = bin(n)[2:]
        return sum(list(map(int,n)))

# 循环检查位运算

class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/er-jin-zhi-zhong-1de-ge-shu-by-leetcode-50bb1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 位运算优化
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/er-jin-zhi-zhong-1de-ge-shu-by-leetcode-50bb1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 递归位运算

class Solution:
    def hammingWeight(self, n: int) -> int:
        return 0 if n <= 0 else 1 + self.hammingWeight(n & (n - 1))