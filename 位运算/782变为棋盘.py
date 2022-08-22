# ctrl c + ctrl v 一气呵成
# Python3+位运算+贪心+模拟+构造
#
# 首先观察发现要满足题意，无论是对于行还是对于列，都必须满足行列组成的二进制数只能是两个，且两个数的位运算互补，且两个数的计数需要正好满足相差最多一个
# 对于xxyyyx和来说要变成目标只能是xyxyxy或者yxyxyx，同时由于只有两个数，与目标位置的编辑距离数一定成对出现，是偶数
# 比如xxyyyx与xyxyxy不同的位置为12451245，只需要交换4/2=2次，因此可以罗列xyxyxy与yxyxyx计算取较小值即可
#
# 作者：liupengsay
# 链接：https://leetcode.cn/problems/transform-to-chessboard/solution/er-xu-cheng-ming-jiu-xu-zui-python3wei-y-nvcr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from collections import Counter


class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        n = len(board)
        # 将行列转为二进制数：交换行列不会影响位运算的异或运算与与运算
        row = []
        for i in range(n):
            for j in range(n):
                board[i][j] = str(board[i][j])
            row.append(int("0b" + "".join(board[i]), 2))

        col = []
        for j in range(n):
            col.append(int("0b" + "".join([board[i][j] for i in range(n)]), 2))

        def check(lst):
            cnt = Counter(lst)
            x, y = min(cnt), max(cnt)
            # 不满足条件：只有两个数
            if len(cnt) != 2:
                return -1
            # 不满足条件：位运算不是互补
            if x & y or x ^ y != (1 << n) - 1:
                return -1
            # 不满足条件：奇偶个数
            if n % 2 == 0:
                if cnt[x] != cnt[y]:
                    return -1
            else:
                if abs(cnt[x] - cnt[y]) != 1:
                    return -1
            # 列举可能的顺序组合：计算需要操作的次数
            lst1 = []
            lst2 = []
            for k in range(n):
                if k % 2:
                    lst1.append(x)
                    lst2.append(y)
                else:
                    lst1.append(y)
                    lst2.append(x)
            # 贪心比较不同位置的个数：由于两个数一定是成对出现所以除以2即为操作次数
            if Counter(lst1) == cnt:
                cost1 = sum(int(lst[k] != lst1[k]) for k in range(n)) // 2
            else:
                cost1 = n + 1
            if Counter(lst2) == cnt:
                cost2 = sum(int(lst[k] != lst2[k]) for k in range(n)) // 2
            else:
                cost2 = n + 1
            return min(cost1, cost2)

        row_cost = check(row)
        col_cost = check(col)
        if row_cost == -1 or col_cost == -1:
            return -1
        return row_cost + col_cost

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # 棋盘的第一行与第一列
        rowMask = colMask = 0
        for i in range(n):
            rowMask |= board[0][i] << i
            colMask |= board[i][0] << i
        reverseRowMask = ((1 << n) - 1) ^ rowMask
        reverseColMask = ((1 << n) - 1) ^ colMask
        rowCnt = colCnt = 0
        for i in range(n):
            currRowMask = currColMask = 0
            for j in range(n):
                currRowMask |= board[i][j] << j
                currColMask |= board[j][i] << j
            # 检测每一行和每一列的状态是否合法
            if currRowMask != rowMask and currRowMask != reverseRowMask or \
               currColMask != colMask and currColMask != reverseColMask:
                return -1
            rowCnt += currRowMask == rowMask  # 记录与第一行相同的行数
            colCnt += currColMask == colMask  # 记录与第一列相同的列数

        def getMoves(mask: int, count: int) -> int:
            ones = mask.bit_count()
            if n & 1:
                # 如果 n 为奇数，则每一行中 1 与 0 的数目相差为 1，且满足相邻行交替
                if abs(n - 2 * ones) != 1 or abs(n - 2 * count) != 1:
                    return -1
                if ones == n // 2:
                    # 偶数位变为 1 的最小交换次数
                    return n // 2 - (mask & 0xAAAAAAAA).bit_count()
                else:
                    # 奇数位变为 1 的最小交换次数
                    return (n + 1) // 2 - (mask & 0x55555555).bit_count()
            else:
                # 如果 n 为偶数，则每一行中 1 与 0 的数目相等，且满足相邻行交替
                if ones != n // 2 or count != n // 2:
                    return -1
                # 偶数位变为 1 的最小交换次数
                count0 = n // 2 - (mask & 0xAAAAAAAA).bit_count()
                # 奇数位变为 1 的最小交换次数
                count1 = n // 2 - (mask & 0x55555555).bit_count()
                return min(count0, count1)

        rowMoves = getMoves(rowMask, rowCnt)
        colMoves = getMoves(colMask, colCnt)
        return -1 if rowMoves == -1 or colMoves == -1 else rowMoves + colMoves
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/transform-to-chessboard/solution/bian-wei-qi-pan-by-leetcode-solution-39dd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
if __name__ == '__main__':
    board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
    sol = Solution()
    print(sol.movesToChessboard(board))