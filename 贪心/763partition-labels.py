# 贪心算法，当我们找到一个partition的时候，就将其记录下来
# 速度击败99%


from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        record = defaultdict(list)
        for i, val in enumerate(s):
            record[val].append(i)
        ans = []
        max_idx, last = 0, -1
        for i, val in enumerate(s):
            if record[val][-1] > max_idx:
                max_idx = record[val][-1]

            if i == max_idx:
                ans.append(max_idx-last)
                last = max_idx
        return ans


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition

#
# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / partition - labels / solution / hua - fen - zi - mu - qu - jian - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。