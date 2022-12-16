class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        notes:  sort, then lptr rptr
                need inner while loop to avoid duplicate b,c in a+b+c
        '''
        nums.sort()
        res = []
        
        prev = nums[0] + 1
        for i in range(len(nums)-2):
            if nums[i] == prev:
                continue
            prev = nums[i]
            
            l, r = i+1, len(nums)-1
            while l != r:
                a = [nums[i], nums[l], nums[r]]
                s = sum(a)
                
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append(a)
                    l += 1
                    while nums[l] == nums[l-1] and l != r:
                        l += 1
        return res