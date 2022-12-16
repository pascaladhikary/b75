class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        notes:  nth step: (n-1) or (n-2)
                subproblem: steps to i 
                 0 1 2 3 4 5
                [0 1 2 3 5 8] - can hold last two after initial 3
                can also just top down recurse
        '''
        memo = {0:0, 1:1, 2:2}
        
        if n in memo: return memo[n]
        
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
            
        return memo[n]