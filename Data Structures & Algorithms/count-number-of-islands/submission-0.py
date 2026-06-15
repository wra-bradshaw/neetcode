class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited: list[list[bool]] = [[False for _ in range(len(grid[i]))] for i in range(len(grid))]

        def dfs(i: int, j: int):
            visited[i][j] = True

            if i-1 >= 0:
                if grid[i-1][j] == "1" and not visited[i-1][j]:
                    dfs(i-1, j)
            if i+1 < len(grid):
                if grid[i+1][j] == "1" and not visited[i+1][j]:
                    dfs(i+1, j)
            if j-1 >= 0:
                if grid[i][j-1] == "1" and not visited[i][j-1]:
                    dfs(i, j-1)
            if j+1 < len(grid[i]):
                if grid[i][j+1] == "1" and not visited[i][j+1]:
                    dfs(i, j+1)
        
        n_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not visited[i][j]:
                    n_islands += 1
                    visited[i][j] = True

                    dfs(i, j)

        return n_islands







        