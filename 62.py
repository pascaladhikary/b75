class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        notes:  subproblem: number of unique paths to i, j
                check above and left 
        '''
        memo = [[0] * (n+1) for _ in range(m+1)]
        memo[0][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                memo[i][j] = memo[i][j-1] + memo[i-1][j]

        return memo[m][n]