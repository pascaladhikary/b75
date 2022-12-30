class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        notes:  subproblem: longest common ss ending at i, j
                2d memo, let row/col 0 be zeros
                if t[i]==t[j], 1 + diagonal since we can't use either of the chars
                else max(up/left/diagonal), but diag is forced < up/left
        '''
        m, n = len(text1)+1, len(text2)+1
        memo = [[0] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        
        return memo[-1][-1]