class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        notes:  subproblem: largest sum ending at i-1
        crux:   if sum dips below 0, reset
        '''
        m = [nums[0]] + [0] * (len(nums)-1)
        
        for i in range(1, len(nums)):
            if m[i-1] > 0:
                m[i] = m[i-1] + nums[i]
            else:
                m[i] = nums[i]

        return max(m)