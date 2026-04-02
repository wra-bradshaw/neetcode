class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        sorted_nums = sorted(nums)
        
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            lower = i + 1
            upper = len(sorted_nums) -1
            
            while upper > lower:                
                num_sum = sorted_nums[lower] + sorted_nums[upper] + sorted_nums[i]

                if num_sum == 0:
                    arr = [sorted_nums[i], sorted_nums[lower], sorted_nums[upper]]
                    result.append(arr)
                    upper -= 1
                    lower += 1

                    while upper > lower and sorted_nums[upper] == sorted_nums[upper + 1]:
                        upper -= 1
                    while upper > lower and sorted_nums[lower] == sorted_nums[lower - 1]:
                        lower += 1
                elif num_sum > 0:
                    upper -= 1
                else:
                    lower += 1
                
        return result