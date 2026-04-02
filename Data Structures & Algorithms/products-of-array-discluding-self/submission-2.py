class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        helper: List[List[int]] = [[1, 1] for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            helper[i][0] = helper[i-1][0] * nums[i-1] 
        
        for i in range(len(nums)-2, -1, -1):
            helper[i][1] = helper[i+1][1] * nums[i+1]

        res: List[int] = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = helper[i][0] * helper[i][1]

        return res
