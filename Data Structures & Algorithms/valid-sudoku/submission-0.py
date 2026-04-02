class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_status: List[List[bool]] = [[False] * 9 for _ in range(9)]
        col_status: List[List[bool]] = [[False] * 9 for _ in range(9)]
        box_status: List[List[List[bool]]] = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for row_i, row in enumerate(board):
            for col_i, col in enumerate(row):
                if col == ".":
                    continue
                num = int(col) - 1
                box_row_i = math.floor(row_i/3)
                box_col_i = math.floor(col_i/3)
                
                if row_status[row_i][num] or col_status[col_i][num] or box_status[box_row_i][box_col_i][num]:
                    return False
                
                row_status[row_i][num] = True
                col_status[col_i][num] = True
                box_status[box_row_i][box_col_i][num] = True
        
        return True
            
                



