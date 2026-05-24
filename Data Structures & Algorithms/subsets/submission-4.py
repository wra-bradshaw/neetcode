class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = [[]]

        def recurse(curr: list[int], i: int):
            for j in range(i+1, len(nums)):
                curr.append(nums[j])
                res.append(curr.copy())
                recurse(curr, j)
                curr.pop()

        for i in range(0, len(nums)):
            curr = [nums[i]]
            res.append(curr.copy())
            recurse(curr, i)
        
        return res
