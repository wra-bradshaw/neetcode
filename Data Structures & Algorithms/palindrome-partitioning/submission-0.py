# "hannahernie"

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: list[list[str]] = []
        palindromes: list[str] = []
        
        def backtrack(lower: int, upper: int):
            if upper > len(s):
                if lower > len(s) - 1:
                    res.append(palindromes.copy())
                return
            if self.is_palindrome(s[lower:upper]):
                palindromes.append(s[lower:upper])
                backtrack(upper, upper+1)
                palindromes.pop()
            backtrack(lower, upper+1)

        backtrack(0, 1)

        return res

    def is_palindrome(self, s: str):
        return s == s[::-1]




