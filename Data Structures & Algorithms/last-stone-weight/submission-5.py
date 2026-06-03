import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x-y > 0:
                heapq.heappush_max(stones, x-y)
        
        return stones[0] if len(stones) > 0 else 0

            

        