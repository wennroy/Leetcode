class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        traveled_1 = [-1] * n
        traveled_2 = [-1] * n

        nxt = node1
        step = 0
        traveled_1[nxt] = step
        while edges[nxt] != -1 and traveled_1[edges[nxt]] == -1:
            nxt = edges[nxt]
            step += 1
            traveled_1[nxt] = step

        nxt = node2
        step = 0
        traveled_2[nxt] = step
        while edges[nxt] != -1 and traveled_2[edges[nxt]] == -1:
            nxt = edges[nxt]
            step += 1
            traveled_2[nxt] = step

        min_step = 10 ** 5
        ans = -1
        for i in range(n):
            if traveled_1[i] == -1 or traveled_2[i] == -1:
                continue
            max_step = max(traveled_1[i], traveled_2[i])
            if min_step > max_step:
                min_step = max_step
                ans = i
        return ans
