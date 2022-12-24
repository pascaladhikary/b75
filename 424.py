class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        notes:  hold freq
                check max in dict at each window
        crux:   r-l+1 - max occurence <= k
        '''
        l, r = 0, 0
        freq = collections.defaultdict(int)
        res = 0

        while r != len(s):
            freq[s[r]] += 1
            m = max(freq.values())

            if r-l+1-m > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            r += 1

        return res