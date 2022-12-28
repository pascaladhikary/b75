class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        notes   subproblem: fewest coins to amount i
                amount i = 1 + min path out of i - c1, c2, c3 else -1
                 0 1 2 3 4 5 6 7    coins = [1, 2, 5]
                [0 1 1 2 2 1 2 2]
        crux:   let 0 be the only base, otherwise let impossible be -1
        '''
        
        n = amount + 1
        memo = [-1] * n
        memo[0] = 0

        for i in range(1, n):
            res = float('inf')
            for c in coins:
                if i-c >= 0 and memo[i-c] != -1:
                    res = min(res, memo[i-c])
            
            if res != float('inf'):
                memo[i] = res + 1

        return memo[-1]