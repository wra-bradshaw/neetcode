class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
    def binary_search(self, nums: List[int], start: int, end: int, target: int) -> int:
        if end - start <= 0:
            if nums[start] == target:
                return start
            return -1
            
        mid = start + math.trunc((end - start) / 2)
        print("chose: ", mid, ", and it is ", nums[mid])
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, start, mid, target)
        else:
            return self.binary_search(nums, mid + 1, end, target)