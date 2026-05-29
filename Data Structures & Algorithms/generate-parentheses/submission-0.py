class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []

        def backtrack(n_currently_open: int, n_currently_closed: int, state: str):
            if n_currently_closed >= n:
                res.append(state)
                return
            if n_currently_open < n:
                backtrack(n_currently_open + 1, n_currently_closed, state + "(")
            if n_currently_closed < n_currently_open:
                backtrack(n_currently_open, n_currently_closed + 1, state + ")")

        backtrack(0, 0, "")
        
        return res
        
            