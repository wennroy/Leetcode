# BFS或者DFS遍历即可得到答案。由于没注意0本身也是一个点，导致结果出现了微小偏差。
# 在将0的结点放入到stack中时，也忘记在restricted_set里面添加0，导致又错了一次
from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        nxt_dict = defaultdict(set)
        for edge in edges:
            nxt_dict[edge[0]].add(edge[1])
            nxt_dict[edge[1]].add(edge[0])
        stack = list(nxt_dict[0])
        restricted_set = set(restricted)
        ans = 1
        restricted_set.add(0)
        while stack:
            nxt_pt = stack.pop()
            if nxt_pt in restricted_set:
                continue
            ans += 1
            restricted_set.add(nxt_pt)
            for pt in nxt_dict[nxt_pt]:
                if pt not in restricted_set:
                    stack.append(pt)

        return ans