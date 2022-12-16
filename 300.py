class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        notes:  subproblem: max subsequence ending at i
                memo[i] = 1 + max len where val j < val i
        '''
        n = len(nums)
        memo = [0] * n
        
        for i in range(n):
            filtered = []
            for j in range(i):
                if nums[j] < nums[i]:
                    filtered.append(memo[j])
            memo[i] = 1 + max(filtered, default=0)
    
        return max(memo)