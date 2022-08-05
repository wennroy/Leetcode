class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        traveled = [-1] * n
        max_node = -1
        for i in range(n):
            if traveled[i] == -1:
                nxt = i
                cur_traveled = []
                cur_cycle_len = -1
                while edges[nxt] != -1 and traveled[edges[nxt]] == -1:
                    cur_traveled.append(nxt)
                    traveled[nxt] = 0
                    nxt = edges[nxt]
                cur_traveled.append(nxt)
                for idx, val in enumerate(cur_traveled):
                    if val == edges[nxt]:
                        cur_cycle_len = len(cur_traveled) - idx
                        break

                if cur_traveled and cur_cycle_len > max_node:
                    max_node = cur_cycle_len

        return max_node



