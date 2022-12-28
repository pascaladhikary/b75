class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        notes:  subproblem: maximum product ending at i
                two memos, max and min
                intuition is really pos and neg memo
        crux:   include nums[i] bc [-1, 2]
        '''
        n = len(nums)
        min_ = [0] * n
        max_ = [0] * n
        min_[0] = max_[0] = nums[0]
        
        for i in range(1, n):
            max_[i] = max(nums[i] * min_[i-1], nums[i] * max_[i-1], nums[i])
            min_[i] = min(nums[i] * min_[i-1], nums[i] * max_[i-1], nums[i])

        return max(max_)