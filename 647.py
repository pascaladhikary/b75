class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        notes:  palindrome l == r
                expand at each letter, even and odd case
        '''
        res = 0
        
        for i in range(len(s)):
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
            l, r = i, i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
        return res