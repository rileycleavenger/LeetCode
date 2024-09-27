class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, grid):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == '2' or grid[i][j] == '0':
                return
            
            grid[i][j] = '2'
            
            dfs(i+1, j, grid)
            dfs(i-1, j, grid)
            dfs(i, j+1, grid)
            dfs(i, j-1, grid)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j, grid)
                    count +=1
                    
        return count
        