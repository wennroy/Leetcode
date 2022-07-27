# 超慢写法 排序+哈希表
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        record = defaultdict(list)
        for i, val in enumerate(arr):
            record[val].append(i)
        sorted_arr = sorted(arr)
        rank = 0
        ans = [0] * n
        last = None
        for i, val in enumerate(sorted_arr):
            if val == last:
                rank -= 1
            rank += 1
            last = val
            ans[record[val].pop()] = rank
        return ans


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[v] for v in arr]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/rank-transform-of-an-array/solution/shu-zu-xu-hao-zhuan-huan-by-leetcode-sol-8zlu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

