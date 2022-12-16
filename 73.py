class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        notes:  dfs, add i, j to seen after expand directionally
        crux:   do not add to seen if originally zero
        '''
        r, c = len(matrix), len(matrix[0])
        
        def zero(i, j, d):
            if not (-1 < i < r and -1 < j < c):
                return
            
            if matrix[i][j] != 0:
                seen.add((i, j))
                matrix[i][j] = 0
                
            x, y = d
            zero(i+y, j+x, d)
            
        seen = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(r):
            for j in range(c):
                if (i, j) not in seen and matrix[i][j] == 0:
                    for x, y in directions: 
                        zero(i+y, j+x, (x,y))
                    seen.add((i, j))