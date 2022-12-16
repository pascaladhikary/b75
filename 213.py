class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        notes:  run it twice, one [1:len], one [0:len-1]
        '''
        def rob1(nums):
            n = len(nums)
            if n == 1: return nums[0]

            memo = [0] * n
            memo[0] = nums[0]
            memo[1] = max(nums[1], nums[0])

            for i in range(2, n):
                    memo[i] = max(nums[i] + memo[i-2], memo[i-1])

            return memo[-1]

        return max(rob1(nums[1:]), rob1(nums[:-1])) if len(nums) != 1 else nums[0]  