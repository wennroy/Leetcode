
from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 找到第一座岛
        first_island = set()
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        flag = False
        for i in range(n):
            if flag:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    pts = set()
                    pts.add((i,j))
                    while pts:
                        nxt_pts = set()
                        for x, y in pts:
                            first_island.add((x,y))
                            for a, b in DIRS:
                                new_x = x + a
                                new_y = y + b
                                if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 1 and (new_x, new_y) not in first_island:
                                    nxt_pts.add((new_x, new_y))
                        pts = nxt_pts
                    flag = True
                    break
        pts = first_island
        used = set()
        ans = 0
        while pts:
            nxt_pts = set()
            for x, y in pts:
                used.add((x,y))
                for a, b in DIRS:
                    new_x = x + a
                    new_y = y + b
                    if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in used and (new_x, new_y) not in first_island:
                        if grid[new_x][new_y] == 1:
                            return ans
                        nxt_pts.add((new_x, new_y))
            pts = nxt_pts
            ans += 1


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(sol.shortestBridge(grid))