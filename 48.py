class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        notes:  reverse shift to hold temp, 
                7->1, 9->7, 3->6, 1->3
        crux:   l < r because at even base case l/r cross over
        '''
        n = len(matrix)
        l, r = 0, n-1
        
        while l < r:
            for i in range(r-l):
                t, b = l, r

                temp = matrix[t][l+i]

                matrix[t][l+i] = matrix[b-i][l]

                matrix[b-i][l] = matrix[b][r-i]

                matrix[b][r-i] = matrix[t+i][r]

                matrix[t+i][r] = temp
            l += 1
            r -= 1