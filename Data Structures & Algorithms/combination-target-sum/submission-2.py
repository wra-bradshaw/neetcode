class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int):
            s = sum(subset)
            if i >= len(nums) or s >= target:
                if s == target:
                    res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res
