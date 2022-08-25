#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型 the n
# @return int整型
#
class Solution:
    # 判断皇后是否符合条件
    def isValid(self, pos: List[int], row: int, col: int):
        # 遍历所有已经记录的行
        for i in range(row):
            # 不能同行同列同一斜线
            if row == i or col == pos[i] or abs(row - i) == abs(col - pos[i]):
                return False
        return True

    # 递归查找皇后种类
    def recursion(self, n: int, row: int, pos: List[int], res: int):
        # 完成全部行都选择了位置
        if row == n:
            res += 1
            return int(res)
        # 遍历所有列
        for i in range(n):
            # 检查该位置是否符合条件
            if self.isValid(pos, row, i):
                # 加入位置
                pos[row] = i
                # 递归继续查找
                res = self.recursion(n, row + 1, pos, res)
        return res

    def Nqueen(self, n: int) -> int:
        res = 0
        # 下标为行号，元素为列号，记录皇后位置
        pos = [0] * n
        # 递归
        result = self.recursion(n, 0, pos, res)
        return result


