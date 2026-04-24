class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            if nums[abs(n) - 1] < 0:
                return abs(n)
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        
        for i in range(0, len(nums)):
            nums[i] = abs(nums[i])

