class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        from sortedcontainers import SortedDict

        area_record = SortedDict()
        m, n = len(isInfected), len(isInfected[0])
        visited = [[-1] * n for _ in range(m)]

        def dfs(i, j, group_id):
            if isInfected[i][j] != 1 and visited[i][j] != -1:
                return False
            else:
                visited[i][j] = group_id
                px = [-1, 1, 0, 0]
                py = [0, 0, -1, 1]
                for k in range(4):
                    x, y = px[k], py[k]
                    new_x = x + i
                    new_y = y + j
                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                        if isInfected[new_x][new_y] != 1:
                            attempt_area.add((new_x, new_y))
                        if visited[new_x][new_y] == -1 and isInfected[new_x][new_y] == 1:
                            dfs(new_x, new_y, group_id)
                return True

        for i in range(m):
            for j in range(n):
                if visited[i][j] != -1:
                    continue
                if isInfected[i][j] == 1:
                    if not area_record.keys():
                        group_id = 0
                    else:
                        group_id = area_record.keys()[-1] + 1
                    attempt_area = set()
                    dfs(i, j, group_id)
                    area_record[group_id] = len(attempt_area)
                    print(attempt_area)
                    print(area_record)

        print(area_record)
        print(visited)
        print(isInfected)
        return 0

isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
k = Solution()
k.containVirus(isInfected)

# 抄答案拿了个双百emmm

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        while True:
            neighbors, firewalls = list(), list()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        q = deque([(i, j)])
                        neighbor = set()
                        firewall, idx = 0, len(neighbors) + 1
                        isInfected[i][j] = -idx

                        while q:
                            x, y = q.popleft()
                            for d in range(4):
                                nx, ny = x + dirs[d][0], y + dirs[d][1]
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 1:
                                        q.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                                    elif isInfected[nx][ny] == 0:
                                        firewall += 1
                                        neighbor.add((nx, ny))

                        neighbors.append(neighbor)
                        firewalls.append(firewall)

            if not neighbors:
                break

            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            ans += firewalls[idx]
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2

            for i, neighbor in enumerate(neighbors):
                if i != idx:
                    for x, y in neighbor:
                        isInfected[x][y] = 1

            if len(neighbors) == 1:
                break

        return ans

#
# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / contain - virus / solution / ge - chi - bing - du - by - leetcode - solution - vn9m /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。