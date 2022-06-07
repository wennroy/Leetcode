class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        import numpy as np
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        if not points[0][0] == points[1][0]:
            k1 = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0])
        else:
            k1 = np.inf
        if not points[2][0] == points[1][0]:
            k2 = (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])
        else:
            k2 = np.inf

        if k1 == k2:
            return False
        else:
            return True

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        v2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
        return v1[0] * v2[1] - v1[1] * v2[0] != 0

'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/valid-boomerang/solution/you-xiao-de-hui-xuan-biao-by-leetcode-so-yqby/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''