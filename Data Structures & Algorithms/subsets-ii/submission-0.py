class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res: list[list[int]] = []
        subset: list[int] = []

        def dfs(i: int):
            res.append(subset.copy())
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()
            
        dfs(0)
        return res