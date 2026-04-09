class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMinSearch(nums, 0, len(nums)-1)

    def findMinSearch(self, nums: list[int], start: int, end: int) -> int:
        if end - start <= 1:
            return min(nums[start], nums[end])
        midpoint = start + math.floor((end-start)/2)
        if nums[midpoint] > nums[end]:
            return self.findMinSearch(nums, midpoint, end)
        else:
            return self.findMinSearch(nums, start, midpoint)
