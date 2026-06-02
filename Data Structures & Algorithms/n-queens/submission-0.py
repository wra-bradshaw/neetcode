class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col_is_clear = [True] * n
        pos_diag_is_clear = [True] * (2 * n - 1)
        neg_diag_is_clear = [True] * (2 * n - 1)
        
        board = [["."] * n for _ in range(n)]
        res = []
        
        def backtrack(r: int):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                pos_i = r + c
                neg_i = r - c + (n - 1)
                
                if col_is_clear[c] and pos_diag_is_clear[pos_i] and neg_diag_is_clear[neg_i]:
                    board[r][c] = "Q"
                    col_is_clear[c] = False
                    pos_diag_is_clear[pos_i] = False
                    neg_diag_is_clear[neg_i] = False
                    
                    backtrack(r + 1)
                    
                    board[r][c] = "."
                    col_is_clear[c] = True
                    pos_diag_is_clear[pos_i] = True
                    neg_diag_is_clear[neg_i] = True
        
        backtrack(0)
        return res