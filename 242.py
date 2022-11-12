class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        notes:  check empty hmap
        '''
        freq = collections.defaultdict(int)
        
        for c in s:
            freq[c] += 1
        
        for c in t:
            if c not in freq:
                return False
            freq[c] -= 1
            if freq[c] == 0:
                freq.pop(c)
        
        return not freq