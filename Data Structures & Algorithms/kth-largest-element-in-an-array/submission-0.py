import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify_max(nums)

        for _ in range(k-1):
            heapq.heappop_max(nums)

        return heapq.heappop_max(nums)

        

        
        