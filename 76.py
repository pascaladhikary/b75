class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        notes:  two ptr sliding window
        crux:   we have to replace our last shrinked character
                while doing so we further decrement target frequencies
                so when we shrink, we can get rid of duplicates
        '''
        freq = collections.Counter(t)

        l, r = 0, 0
        n, m = len(s), len(t)
        res = ""

        while r != n:
            c = s[r]
            if c in freq:
                if freq[c] > 0: m -= 1
                freq[c] -= 1

            if m == 0:
                while True:
                    c = s[l]
                    if c in freq: freq[c] += 1
                    if freq[c] > 0: break
                    l += 1

                if r-l+1 < len(res) or res == "": 
                    res = s[l:r+1]
                l += 1
                m += 1

            r += 1
                    
        return res