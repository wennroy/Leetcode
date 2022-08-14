class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        from sortedcontainers import SortedDict
        table = SortedDict()
        for score, pt in enumerate(edges):
            if pt not in table.keys():
                table[pt] = score
            else:
                table[pt] += score
        max_idx, max_score = 0, -1
        for idx in table.keys():
            if table[idx] > max_score:
                max_idx = idx
                max_score = table[idx]

        return max_idx