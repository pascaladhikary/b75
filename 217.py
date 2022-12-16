class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        notes:  set
        '''
        s = set()
        
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False