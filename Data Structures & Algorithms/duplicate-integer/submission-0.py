class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict: dict[int, bool] = {}
        for num in nums:
            if num in nums_dict:
                return True
            else:
                nums_dict[num] = True
        return False

        