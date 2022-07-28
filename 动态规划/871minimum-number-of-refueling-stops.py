# 硬刚，超出时间限制
from collections import defaultdict


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = defaultdict(list)
        travel_dist = stations[0][0] if stations else target
        dp[0].append((0, startFuel - travel_dist))  # 到第i+1个加油站时，已经停的次数和剩余的油量
        if dp[0][0][1] < 0:
            return -1

        for i, val in enumerate(stations, start=1):
            if i >= n:
                travel_dist = target - stations[-1][0]
            else:
                travel_dist = stations[i][0] - stations[i - 1][0]
            for (stop_num, fuel_remain) in dp[i - 1]:
                nxt_fuel_remain = fuel_remain - travel_dist
                if nxt_fuel_remain >= 0:
                    if not (stop_num, nxt_fuel_remain) in dp[i]:
                        dp[i].append((stop_num, nxt_fuel_remain))
                    if not (stop_num + 1, nxt_fuel_remain + stations[i - 1][1]) in dp[i]:
                        dp[i].append((stop_num + 1, nxt_fuel_remain + stations[i - 1][1]))
                elif nxt_fuel_remain + stations[i - 1][1] >= 0:
                    if not (stop_num + 1, nxt_fuel_remain + stations[i - 1][1]) in dp[i]:
                        dp[i].append((stop_num + 1, nxt_fuel_remain + stations[i - 1][1]))
                else:
                    continue
            print(dp)
            if not dp[i]:
                return -1
            dp.pop(i - 1)
        min_stop = n
        for s in dp[n]:
            if s[0] < min_stop:
                min_stop = s[0]
        return min_stop


# 改为set，有几个超出时间限制能过了！
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = defaultdict(set)
        travel_dist = stations[0][0] if stations else target
        if startFuel - travel_dist < 0:
            return -1
        dp[0].add((0, startFuel - travel_dist))  # 到第i+1个加油站时，已经停的次数和剩余的油量

        for i, val in enumerate(stations, start=1):
            if i >= n:
                travel_dist = target - stations[-1][0]
            else:
                travel_dist = stations[i][0] - stations[i - 1][0]
            for (stop_num, fuel_remain) in dp[i - 1]:
                nxt_fuel_remain = fuel_remain - travel_dist
                if nxt_fuel_remain >= 0:
                    dp[i].add((stop_num, nxt_fuel_remain))
                    dp[i].add((stop_num + 1, nxt_fuel_remain + stations[i - 1][1]))
                elif nxt_fuel_remain + stations[i - 1][1] >= 0:
                    dp[i].add((stop_num + 1, nxt_fuel_remain + stations[i - 1][1]))
                else:
                    continue
            if not dp[i]:
                return -1
            dp.pop(i - 1)
        min_stop = n
        for s in dp[n]:
            if s[0] < min_stop:
                min_stop = s[0]
        return min_stop

# 丑陋的动态规划

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        n = len(stations)
        dp = [[0] * n for _ in range(n)]  # 经过第i个加油站的时候，加了j次油最多可以跑多远
        dp[0][0] = startFuel
        diff_arr = []
        last = 0
        for i, s in enumerate(stations):
            diff_arr.append(s[0] - last)
            last = s[0]
        for i in range(1, n):
            for j in range(i + 1):
                if j != 0 and dp[i - 1][j - 1] >= diff_arr[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + stations[i - 1][1]) - diff_arr[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j] - diff_arr[i - 1]
                if dp[i][j] < 0:
                    dp[i][j] = -math.inf

        if dp[n - 1][n - 1] < diff_arr[-1]:
            return -1
        for j in range(n):
            if dp[n - 1][j] >= diff_arr[-1]:
                return j



'''
我觉得吧，官方题解的动态规划写得并不好，没有从最基本的状态转移方程开始推导，直接把二维的状态压缩成一维的，这对很多朋友都不够友好。

贴一个二维状态定义的动态规划。

状态定义： dp[i][j] 表示对于 [0, i - 1] 范围内的加油站，最多加 j 次油能够到达的最远距离。

初始化条件： （1）当 j == 0 时，此时有 dp[i][0] = startFuel。 （2）当 i < j 时，这种情况其实是不存在的，因为总共只有 i 个加油站却需要加 j 次油，设成 0 代表不存在。

状态转移方程： （1）我们可以选择在第 i - 1 个加油站加油，此时 dp[i][j] = dp[i - 1][j - 1] + stations[i - 1][1]。当然能进行这个状态转移的条件是dp[i - 1][j - 1] >= stations[i - 1][0]，因为必须要到达第 i - 1 个加油站才能选择在第 i - 1 个加油站加油与否。 
（2）我们也可以选择不在第 i - 1 个加油站加油，此时的状态转移方程更简单，是dp[i][j] = dp[i - 1][j]。 取上述 2 种情况的最大值就是我们的 dp[i][j]。

为了降低大家的理解难度，用记忆化搜索的方式实现了上述动态规划解法，其中的 helper(i, j) 函数就对应上文分析中的状态定义 dp[i][j]。

时间复杂度和空间复杂度均是 O(n ^ 2)。

'''

# 标答动态规划
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        return next((i for i, v in enumerate(dp) if v >= target), -1)



# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/minimum-number-of-refueling-stops/solution/zui-di-jia-you-ci-shu-by-leetcode-soluti-nmga/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 贪心算法

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        ans, fuel, prev, h = 0, startFuel, 0, []
        for i in range(n + 1):
            curr = stations[i][0] if i < n else target
            fuel -= curr - prev
            while fuel < 0 and h:
                fuel -= heappop(h)
                ans += 1
            if fuel < 0:
                return -1
            if i < n:
                heappush(h, -stations[i][1])
                prev = curr
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/minimum-number-of-refueling-stops/solution/zui-di-jia-you-ci-shu-by-leetcode-soluti-nmga/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。