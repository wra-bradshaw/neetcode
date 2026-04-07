class OneDimensionalised:
    matrix: list[list[int]]
    n: int
    m: int

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix
        self.n = len(matrix)
        if len(matrix) > 0:
            self.m = len(matrix[0])
        else:
            self.m = 0
    
    def __getitem__(self, index) -> int:
        return self.matrix[math.floor(index/self.m)][index%self.m]

    def __len__(self) -> int:
        return self.n*self.m

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m: OneDimensionalised = OneDimensionalised(matrix)
        return self.binary_search(m, 0, len(m) - 1, target) != -1

    def binary_search(self, nums: OneDimensionalised, start: int, end: int, target: int) -> int:
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

