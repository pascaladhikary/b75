class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        notes:  shrink bounds
        crux:   when ending with a row/column matrix break after 
                first row/col traversal otherwise bottom/left issue 
        '''
        
        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix)-1
        
        m = matrix
        res = []

        while l <= r and t <= b:
            for i in range(l, r+1):
                res.append(m[t][i])
            t += 1
            
            for i in range(t, b+1):
                res.append(m[i][r])
            r -= 1

            if not (l <= r and t <= b):
                break

            for i in range(r, l-1, -1):
                res.append(m[b][i])
            b -= 1

            for i in range(b, t-1, -1):
                res.append(m[i][l])
            l += 1

        return res