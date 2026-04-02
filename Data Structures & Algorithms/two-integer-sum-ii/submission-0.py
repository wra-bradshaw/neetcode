class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower = 0
        upper = len(numbers) - 1

        while upper > lower:
            sum = numbers[lower] + numbers[upper]
            if sum == target:
                return [lower+1, upper+1]
            elif sum > target:
                upper -= 1
            else:
                lower += 1
        
        raise ValueError("did not contain a valid solution")
            


        