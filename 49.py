class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        notes:  map chars to dict key counts arr [0]*26
        '''
        freq = collections.defaultdict(list)
        
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
              
            freq[tuple(counts)].append(s)
                
        return freq.values()
        