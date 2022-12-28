class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        notes:  subproblem: max subsequence ending at i
                memo[i] = 1 + max len where val j < val i
        '''
        n = len(nums)
        memo = [0] * n
        memo[0] = 1

        for i in range(1, n):
            res = float('-inf')
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, memo[j])

            if res == float('-inf'): res = 0
            memo[i] = res + 1

        return max(memo)