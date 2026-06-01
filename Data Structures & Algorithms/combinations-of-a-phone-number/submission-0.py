class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digints = [int(v) for v in digits]

        digints_to_chars: dict[int, list[str]] = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        res: list[str] = []
        letters: list[str] = []

        def backtrack(i: int):
            if i == len(digints):
                if len(letters) > 0:
                    res.append("".join(letters))
                return
            
            chars = digints_to_chars[digints[i]]

            for c in chars:
                letters.append(c)
                backtrack(i+1)
                letters.pop()
        
        backtrack(0)

        return res
            


        