class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        notes:  hold freq
                check max in dict at each window
        crux:   r-l+1 - max occurence <= k
        '''
        l, r = 0, 0
        res = -1
        
        freq = collections.defaultdict(int)
        while r != len(s):
            freq[s[r]] += 1        
            
            if (r-l+1) - max(freq.values()) <= k:
                res = max(res, r-l+1)
            else:
                freq[s[l]] -= 1
                l += 1
            r += 1
                
        return res