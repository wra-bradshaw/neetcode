from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.rob_top_down(tuple(nums))

    def rob_bottom_up(self, nums: List[int]) -> int:
        table = [0] * len(nums)

        table[0] = nums[0]

        for i in range(1, len(nums)):
            prev = table[i-1]
            before_prev = (table[i-2] if i > 1 else 0) + nums[i]

            table[i] = max(prev, before_prev)

        return table[len(nums)-1]

    @lru_cache(maxsize=None)
    def rob_top_down(self, nums: tuple[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        
        return max(self.rob_top_down(nums[:len(nums)-1]), self.rob_top_down(nums[:len(nums)-2]) + nums[len(nums)-1])


    


        
        