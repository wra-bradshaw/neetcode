class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res = abs(n)
                break
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        
        for i in range(0, len(nums)):
            nums[i] = abs(nums[i])

        print(nums)

        return res
    
