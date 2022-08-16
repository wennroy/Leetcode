# 遍历split_num但添加限制条件。求和数组的均值有一定的规律，当为奇数均值必为整数，当为偶数，均值必为带.5小数。
# 但总体时间不如直接解一元二次方程

import math
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        for split_num in range(target // 2, 1, -1):
            if (target % split_num == 0 and split_num % 2 == 1) or (
                    not target % split_num == 0 and target * 2 % split_num == 0 and split_num % 2 == 0):
                mid_val = math.ceil(target / split_num)
                start_val = mid_val - (split_num // 2)
                if start_val <= 0:
                    continue
                cur_ans = []
                for i in range(int(start_val), int(start_val + split_num)):
                    cur_ans.append(i)
                ans.append(cur_ans)

        return ans

# 可以直接解一元二次方程，直接判断是否为正整数，是的话就放入答案中

class Solution:
    def findContinuousSequence(self, target: int):
        i, j, res = 1, 2, []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res

# 作者：jyd
# 链接：https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/jian-zhi-offer-57-ii-he-wei-s-de-lian-xu-t85z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 同时也可以用双指针
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res

# 作者：jyd
# 链接：https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/jian-zhi-offer-57-ii-he-wei-s-de-lian-xu-t85z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。