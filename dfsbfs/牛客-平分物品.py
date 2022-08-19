# 现在有n个物品，每一个物品都有一个价值，现在想将这些物品分给两个人，要求这两个人每一个人分到的物品的价值总和相同（个数可以不同，总价值相同即可），
# 剩下的物品就需要扔掉，现在想知道最少需要扔多少价值的物品才能满足要求分给两个人。
#
# 要求：时间复杂度O(3^n)，空间复杂度O(n)

# 看到O3n的时间复杂度就应该直接想到暴力遍历。我们这里开辟三个背包，每次往其中一个背包添加一个重物，找出所有符合条件的最终情况。
# 思路与DFS相同。

import sys

T = int(next(sys.stdin).strip())


def dfs(x, n, A, B, Drop):
    global ans
    if Drop > ans:
        return
    if x == n:
        if A == B:
            ans = min(ans, Drop)
    else:
        dfs(x + 1, n, A + a[x], B, Drop)
        dfs(x + 1, n, A, B + a[x], Drop)
        dfs(x + 1, n, A, B, Drop + a[x])
    return


for _ in range(T):
    n = int(next(sys.stdin).strip())
    a = list(map(int, next(sys.stdin).strip().split(' ')))
    ans = 1000000
    dfs(0, n, 0, 0, 0)
    print(ans)
