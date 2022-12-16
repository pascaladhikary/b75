class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        notes:  shrink bounds
        crux:   when ending with a row/column matrix break after 
                first row/col traversal otherwise bottom/left issue 
        '''
        
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        
        res = [] 
        while l < r and t < b:
            for i in range(r-l):
                res.append(matrix[t][l+i])
            t += 1
                
            for i in range(b-t):
                res.append(matrix[t+i][r-1])
            r -= 1
            
            if not (l < r and t < b):
                break
                
            for i in range(r-l):
                res.append(matrix[b-1][r-1-i])
            b -= 1
            
            for i in range(b-t):
                res.append(matrix[b-1-i][l])
            l += 1
            
        return res