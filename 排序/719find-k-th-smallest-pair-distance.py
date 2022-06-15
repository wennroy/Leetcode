'''
方法一：排序 + 二分查找
先将数组 \textit{nums}nums 从小到大进行排序。因为第 kk 小的数对距离必然在区间 [0, \max (\textit{nums}) - \min(\textit{nums})][0,max(nums)−min(nums)] 内，令 \textit{left} = 0left=0，\textit{right} = \max (\textit{nums}) - \min(\textit{nums})right=max(nums)−min(nums)，我们在区间 [\textit{left}, \textit{right}][left,right] 上进行二分。

对于当前搜索的距离 \textit{mid}mid，计算所有距离小于等于 \textit{mid}mid 的数对数目 \textit{cnt}cnt，如果 \textit{cnt} \ge kcnt≥k，那么 \textit{right} = \textit{mid} - 1right=mid−1，否则 \textit{left} = \textit{mid} + 1left=mid+1。当 \textit{left} \gt \textit{right}left>right 时，终止搜索，那么第 kk 小的数对距离为 \textit{left}left。

给定距离 \textit{mid}mid，计算所有距离小于等于 \textit{mid}mid 的数对数目 \textit{cnt}cnt 可以使用二分查找：枚举所有数对的右端点 jj，二分查找大于等于 \textit{nums}[j] - \textit{mid}nums[j]−mid 的最小值的下标 ii，那么右端点为 jj 且距离小于等于 \textit{mid}mid 的数对数目为 j - ij−i，计算这些数目之和。

Python3C++JavaC#CGolangJavaScript


作者：LeetCode-Solution
链接：https://leetcode.cn/problems/find-k-th-smallest-pair-distance/solution/zhao-chu-di-k-xiao-de-shu-dui-ju-chi-by-xwfgf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

from bisect import *

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect_left(nums, num - mid, 0, j)
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)

'''
nums排序后，寻找 num - mid 的数值。 固定范围从0到j避免二次计算。
'''