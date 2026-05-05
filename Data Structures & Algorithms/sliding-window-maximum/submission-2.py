
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        max_heap: list[tuple[int, int]] = []
        res = []
        
        for right in range(0, len(nums)): 
            left = right - k + 1
            heapq.heappush(max_heap, (-nums[right], right))
            print(left, right)

            if left >= 0:
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0][0])
        
        return res



            
            

