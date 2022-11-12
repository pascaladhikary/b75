class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        notes:  res[i] = l[i-1] * r[i+1]
        '''
        l, r = [nums[0]], [nums[-1]]
        n = len(nums)
        
        for i in range(1, n):
            l.append(nums[i] * l[-1])
            r.insert(0, nums[n-i-1] * r[0])
        
        res = [0] * n
        for i in range(n):
            if i == 0: 
                res[i] = r[i+1]
            elif i == n-1: 
                res[i] = l[i-1]
            else:
                res[i] = l[i-1] * r[i+1]
                
        return res