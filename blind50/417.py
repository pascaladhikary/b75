class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        notes:  reverse dfs
        '''
        r, c = len(heights), len(heights[0])
        sp, sa = set(), set()
        
        def isValid(i0, j0, i, j, s):
            if -1 < i < r and -1 < j < c and (i, j) not in s and heights[i][j] >= heights[i0][j0]:
                return True
            else:
                return False
        
        def getValidMoves(i, j, s):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            res = []
            
            for x, y in directions:
                if isValid(i, j, i+x, j+y, s):
                    res.append((i+x, j+y))
            return res
        
        def dfs(i, j, s):
            s.add((i, j))
            for x, y in getValidMoves(i, j, s):
                dfs(x, y, s)
        
        for i in range(r):
            if (i, 0) not in sp: dfs(i, 0, sp)
            if (i, c-1) not in sa: dfs(i, c-1, sa)
        
        for j in range(c):
            if (0, j) not in sp: dfs(0, j, sp)
            if (r-1, j) not in sa: dfs(r-1, j, sa)
                
        return sa.intersection(sp)