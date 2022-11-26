class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        
        for n in nums:
            count = 0
            if n-1 not in nums:
                while n in nums:
                    count += 1
                    n += 1
                res = max(count, res)
        
        return res
                        