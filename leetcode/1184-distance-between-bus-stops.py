# https://leetcode.com/problems/distance-between-bus-stops/
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            first = sum(distance[start:destination])
        else:
            first = sum(distance[destination:start])
        second = sum(distance) - first
        return min(first, second)
