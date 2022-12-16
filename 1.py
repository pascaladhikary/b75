class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        notes:  store complement
        '''
        c = {}
        
        for i, n in enumerate(nums):
            if n in c:
                return [c[n], i]
            c[target-n] = i
            