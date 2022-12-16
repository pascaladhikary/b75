class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        notes:  subproblem: number of ways to reach target n
        '''
        n = target
        memo = [0] * (n+1)
        memo[0] = 1

        for i in range(n+1):
            for j in nums:
                if i-j >= 0:
                    memo[i] += memo[i-j]
        
        return memo[-1]