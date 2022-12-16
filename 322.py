class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        notes   subproblem: fewest coins to amount i
                amount i = 1 + min path out of i - c1, c2, c3 else -1
                 0 1 2 3 4 5 6 7    coins = [1, 2, 5]
                [0 1 1 2 2 1 2 2]
        crux:   let 0 be the only base, otherwise let impossible be -1
        '''
        
        memo = [-1] * (amount+1)
        memo[0] = 0
        
        for i in range(1, amount+1):
            paths = []
            for c in coins:
                if i-c >= 0 and memo[i-c] != -1:
                    paths.append((memo[i-c], i-c))
            
            if paths:
                m = min(paths)[1]
                memo[i] = 1 + memo[m]
                
        return memo[-1]