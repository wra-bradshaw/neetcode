class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join([str(d) for d in digits])
        i = int(s)
        i += 1
        s = str(i)
        return [int(c) for c in s]
