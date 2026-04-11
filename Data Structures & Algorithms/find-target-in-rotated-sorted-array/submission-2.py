class RotatedArray:
    data: list[int]
    offset: int

    def _findMinIdx(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self._findMinIdxSearch(nums, 0, len(nums)-1)

    def _findMinIdxSearch(self, nums: list[int], start: int, end: int) -> int:
        if end - start <= 1:
            if nums[start] > nums[end]:
                return end
            else:
                return start
            
        midpoint = start + math.floor((end-start)/2)
        if nums[midpoint] > nums[end]:
            return self._findMinIdxSearch(nums, midpoint, end)
        else:
            return self._findMinIdxSearch(nums, start, midpoint)

    def __init__(self, data: list[int]) -> None:
        self.offset = self._findMinIdx(data)
        self.data = data
    
    def __len__(self) -> int:
        return len(self.data)
    
    def __getitem__(self, index: int) -> int:
        return self.data[(index + self.offset) % len(self.data)]
    
    def __setitem__(self, index: int, value: int) -> None:
        self.data[(index + self.offset) % len(self.data)] = value

    def __delitem__(self, index: int) -> None:
        length = len(self.data)
        
        if index < 0:
            index += length
            
        if index < 0 or index >= length:
            raise IndexError("RotatedArray assignment index out of range")
        
        actual_idx = (index + self.offset) % length
        
        del self.data[actual_idx]
        
        if actual_idx < self.offset:
            self.offset -= 1
        elif self.offset >= len(self.data):
            self.offset = 0

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __reversed__(self):
        for i in range(len(self) - 1, -1, -1):
            yield self[i]

    def __contains__(self, item: int) -> bool:
        return item in self.data

    def __repr__(self) -> str:
        logical_order = [self[i] for i in range(len(self))]
        return f"RotatedArray({logical_order})"
  
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr = RotatedArray(nums)
        res = self.binary_search(arr, 0, len(nums) - 1, target)
        if res == -1:
            return -1
        else:
            return (res + arr.offset) % len(arr)
    def binary_search(self, nums: RotatedArray, start: int, end: int, target: int) -> int:
        if end - start <= 0:
            if nums[start] == target:
                return start
            return -1
            
        mid = start + math.trunc((end - start) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, start, mid, target)
        else:
            return self.binary_search(nums, mid + 1, end, target)
