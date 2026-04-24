class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap: dict[int, bool] = defaultdict(bool)
        for n in nums: 
            if hashmap[n] == True:
                return n
            hashmap[n] = True
        