class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        ranks = {}
        for i, v in enumerate(sorted_score, 1):
            if i == 1:
                ranks[v] = 'Gold Medal'
            elif i == 2:
                ranks[v] = 'Silver Medal'
            elif i == 3:
                ranks[v] = 'Bronze Medal'
            else:
                ranks[v] = str(i)

        ans = [ranks[v] for v in score]
        return ans


class Solution:
    desc = ("Gold Medal", "Silver Medal", "Bronze Medal")

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key=lambda x: -x[1])
        for i, (idx, _) in enumerate(arr):
            ans[idx] = self.desc[i] if i < 3 else str(i + 1)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/relative-ranks/solution/xiang-dui-ming-ci-by-leetcode-solution-5sua/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。