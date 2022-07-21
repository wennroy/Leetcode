# 又是一题不会写的苦难呢
# 排序+贪心算法
# 创建一个vals数组，来记录满足要求的交集的数字
# 排序时让[1,4]排在[1,3]之前，当 ss 相同时按照 ee 降序来进行排序，这样可以实现在处理与交集集合相交元素个数小于 mm 个的区间 [s_i,e_i]
# 时，保证不足的元素都是在区间的开始部分，即我们可以直接从区间开始部分进行往交集集合中添加元素。
#
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, n, m = 0, len(intervals), 2
        vals = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            j = intervals[i][0]
            for k in range(len(vals[i]), m):
                ans += 1
                for p in range(i - 1, -1, -1):
                    if intervals[p][1] < j:
                        break
                    vals[p].append(j)
                j += 1
        return ans

'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/set-intersection-size-at-least-two/solution/she-zhi-jiao-ji-da-xiao-zhi-shao-wei-2-b-vuiv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''