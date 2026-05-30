class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited: list[list[bool]] = [[False] * len(board[0]) for _ in board]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    res = self.existFromStartingChar(visited, board, i, j, word, 1)
                    visited[i][j] = False
                    if res:
                        return True
        return False


    def existFromStartingChar(self, visited: list[list[bool]], board: List[List[str]], i: int, j: int, word: str, i_word: int) -> bool:
        if i_word == len(word):
            return True

        target_char = word[i_word]

        def visit(i: int, j: int) -> bool:
            if visited[i][j] == False:
                visited[i][j] = True
                res = self.existFromStartingChar(visited, board, i, j, word, i_word+1)
                visited[i][j] = False
                return res
            return False

        if j > 0 and board[i][j-1] == target_char:
            res = visit(i, j-1)
            if res:
                return True
        if i > 0 and board[i-1][j] == target_char:
            res = visit(i-1, j)
            if res:
                return True
        if j < len(board[i]) - 1 and board[i][j+1] == target_char:
            res = visit(i, j+1)
            if res:
                return True
        if i < len(board) - 1 and board[i+1][j] == target_char:
            res = visit(i+1, j)
            if res:
                return True
        
        return False

# ["A","B","C","E"],
# ["S","F","C","S"],
# ["A","D","E","E"]
