class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        notes:  dfs
        '''
        r, c = len(grid), len(grid[0])
        def isValid(i, j):
            if -1 < i < r and -1 < j < c and grid[i][j] == '1':
                return True
            else:
                return False
            
        def getValid(i, j):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            res = []
            for x, y in directions:
                if isValid(i+x, j+y):
                    res.append((i+x, j+y))
            return res
        
        def dfs(i, j):
            grid[i][j] = 'X'
            for x, y in getValid(i, j):
                dfs(x, y)
        
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
                    
        return count