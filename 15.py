class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        notes:  extend twoSum
        crux:   we can sort, rhs must be greater 
        '''
        nums.sort()
        n, res = len(nums), set()
        prev = nums[0] + 1

        for i in range(n):
            if nums[i] == prev:
                continue
            prev = nums[i]

            freq = {}
            target = -1 * nums[i]

            for j in range(i+1, n):
                if nums[j] in freq:
                    res.add((nums[j], freq[nums[j]], -1 * target))
                freq[target-nums[j]] = nums[j]

        return list(res)