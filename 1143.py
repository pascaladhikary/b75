class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        notes:  subproblem: longest common ss ending at i, j
                2d memo, let row/col 0 be zeros
                if t[i]==t[j], 1 + diagonal since we can't use either of the chars
                else max(up/left/diagonal), but diag is forced < up/left
        '''
        m, n = len(text1), len(text2)
        memo = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
                
        return memo[m][n]