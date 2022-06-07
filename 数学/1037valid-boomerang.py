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

