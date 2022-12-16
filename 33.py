class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        notes:  if left is sorted: if l <= v <= m left else right
                [4,5,6,7,0,1,2]
                [7,1,2,3,4,5,6]
        crux:   we have to go left <= since //
        '''
        v = target
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2
            
            if v == nums[m]:
                return m
            
            if nums[l] <= nums[m]:
                if nums[l] <= v < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < v <= nums[r]:
                    l = m + 1 
                else:
                    r = m - 1
                         
        return -1