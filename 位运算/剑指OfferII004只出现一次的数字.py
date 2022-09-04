# 直接哈希表
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return cnt.most_common()[-1][0]

# 二进制位
# (num >> i) & 1 寻找第i位的数字
# ans |= (1 << i) 将第i位设置为1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。