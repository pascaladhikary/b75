class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        notes:  4 5 1 2 3
                5 1 2 3 4
                3 4 5 1 2 
                if m < l subarray left else right
                if l < r min = min(m, l)
        crux:   we know any valid subarray forces l < r
                l <= r since [1] is valid
        '''
        
        res = nums[0]
        l, r = 0, len(nums)-1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            m = (l+r)//2
            res = min(res, nums[m])
            
            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
            
        return res
                