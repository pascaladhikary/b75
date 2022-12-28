class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        notes:  subproblem: largest sum ending at i-1
        crux:   if i-1 is negative just take n
        '''
        n = len(nums)
        memo = [0] * n
        memo[0] = nums[0]

        for i in range(1, n):
            memo[i] = max(nums[i]+memo[i-1], nums[i])

        return max(memo)