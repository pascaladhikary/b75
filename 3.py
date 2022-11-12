class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        notes:  set/window, loop until repeated char removed 
        '''
        l, r = 0, 0
        c = set()
        res = 0
        
        while r != len(s):
            while s[r] in c:
                c.remove(s[l])
                l+=1
            
            res = max(res, r-l+1)
            c.add(s[r])
            r += 1
            
        return res