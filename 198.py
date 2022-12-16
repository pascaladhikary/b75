class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            subproblem: max sum ending at i
            max([i] + [i-2], [i-1])
            either include i, or skip (take i-1)
        '''
        n = len(nums)
        if n == 1: return nums[0]

        memo = [0] * n
        memo[0] = nums[0]
        memo[1] = max(nums[1], nums[0])

        for i in range(2, n):
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])

        return memo[-1]