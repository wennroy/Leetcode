class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            tmp = destination
            destination = start
            start = tmp
        # 确保start < des
        dis1, dis2 = sum(distance[start:destination]), sum(distance[:start]+distance[destination:])
        return min(dis1, dis2)