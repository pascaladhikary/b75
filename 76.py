class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        notes:  two ptr sliding window
        crux:   we have to replace our last shrinked character
                while doing so we further decrement target frequencies
                so when we shrink, we can get rid of duplicates
        '''
        freq = collections.defaultdict(int, dict(collections.Counter(list(t))))
        
        l, r = 0, 0
        rem = len(t)
        res = 0, len(s)+1

        while r != len(s):  
            c = s[r]
            
            if freq[c] > 0:
                rem -= 1
            if c in t: 
                freq[s[r]] -= 1
                
            while rem == 0:
                res = (l, r) if (r-l) < (res[1]-res[0]) else res
                c = s[l]
                
                if c in t: 
                    freq[c] += 1
                if freq[c] > 0:
                    rem += 1
                l += 1
            r += 1
                
        return "" if res[1] == len(s)+1 else s[res[0]:res[1]+1]