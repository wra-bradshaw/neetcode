from typing import Self
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

    def __lt__(self, other: Self) -> bool:
        origin = Point(0, 0)
        return self.distance_from(origin) < other.distance_from(origin)
        
    def distance_from(self, other: Self) -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def to_array(self) -> list[int]:
        return [self.x, self.y]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: list[Point] = [Point(v[0], v[1]) for v in points]
        heapq.heapify(heap)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap).to_array())
        
        return res