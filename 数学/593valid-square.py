class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        center_pt = [(p1[0] + p2[0] + p3[0] + p4[0]) / 4, (p1[1] + p2[1] + p3[1] + p4[1]) / 4]
        all_pts = [p1, p2, p3, p4]
        record = [0, -1, -1, -1]  # 0,1,2,3 对应四个点
        idx = 1
        for i in range(1, 4):
            if center_pt[0] * 2 - p1[0] == all_pts[i][0] and center_pt[1] * 2 - p1[1] == all_pts[i][
                1]:  # check 一边是否中心对称
                record[2] = i
            else:
                record[idx] = i
                idx = 3
        if -1 in record:
            return False

        # check 另一边是否中心对称
        if center_pt[0] * 2 - all_pts[record[1]][0] != all_pts[record[3]][0] or center_pt[1] * 2 - all_pts[record[1]][
            1] != all_pts[record[3]][1]:
            return False

        # abs((y1-y3)/(x1-x3) * (y2-y4)/(x2-x4)) = 1 => abs((y1-y3)*(y2-y4)) = abs((x1-x3)*(x2-x4))

        if not abs(all_pts[0][0] - all_pts[record[2]][0]) == abs(all_pts[record[1]][1] - all_pts[record[3]][1]) and \
                not abs(all_pts[0][1] - all_pts[record[2]][1]) == abs(all_pts[record[1]][0] - all_pts[record[3]][0]):
            return False

        if all_pts[record[1]] == all_pts[record[3]]:
            return False
        return True


# 标答的模块式作答

def checkLength(v1: Tuple[int, int], v2: Tuple[int, int]) -> bool:
    return v1[0] * v1[0] + v1[1] * v1[1] == v2[0] * v2[0] + v2[1] * v2[1]


def checkMidPoint(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    return p1[0] + p2[0] == p3[0] + p4[0] and p1[1] + p2[1] == p3[1] + p4[1]


def calCos(v1: Tuple[int, int], v2: Tuple[int, int]) -> int:
    return v1[0] * v2[0] + v1[1] * v2[1]


def help(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    v1 = (p1[0] - p2[0], p1[1] - p2[1])
    v2 = (p3[0] - p4[0], p3[1] - p4[1])
    return checkMidPoint(p1, p2, p3, p4) and checkLength(v1, v2) and calCos(v1, v2) == 0


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2:
            return False
        if help(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if help(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if help(p1, p4, p2, p3):
            return True
        return False


# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/valid-square/solution/you-xiao-de-zheng-fang-xing-by-leetcode-94t5m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
正方形判定定理是几何学里用于判定一个四边形是否为正方形的判定定理。判别正方形的一般顺序为先说明它是平行四边形；再说明它是菱形（或矩形）；
最后说明它是矩形（或菱形）。那么我们可以从枚举四边形的两条斜边入手来进行判断：

如果两条斜边的中点相同：则说明以该两条斜边组成的四边形为「平行四边形」。
在满足「条件一」的基础上，如果两条斜边的长度相同：则说明以该两条斜边组成的四边形为「矩形」。
在满足「条件二」的基础上，如果两条斜边的相互垂直：则说明以该两条斜边组成的四边形为「正方形」。
'''
