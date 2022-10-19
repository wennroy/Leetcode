class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 有点类似于这个数字向左向右走，我们求得这个k的二进制
        # n = 4 k = 5
        # 0             起始
        # 01            右
        # 01 10         左
        # 01 10 10 01   左
        path = bin(k + ((1 << (n - 1)) - 1))
        ans = 0
        for val in path[3:]:
            if (val == '1' and ans == 0) or (val == '0' and ans == 1):
                ans = 1
            else:
                ans = 0

        return ans

# 方便快捷的递归写法
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (k & 1) ^ 1 ^ self.kthGrammar(n - 1, (k + 1) // 2)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/k-th-symbol-in-grammar/solution/di-kge-yu-fa-fu-hao-by-leetcode-solution-zgwd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 找规律 + 位运算： 翻转次数，直接和n没关系了。
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # return (k - 1).bit_count() & 1
        k -= 1
        res = 0
        while k:
            k &= k - 1
            res ^= 1
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/k-th-symbol-in-grammar/solution/di-kge-yu-fa-fu-hao-by-leetcode-solution-zgwd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

