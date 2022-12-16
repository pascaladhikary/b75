class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        notes:  sub problem: does a seq end at i
                hold end of each word as j in memo
                if [j:i] in words then add i+1
        crux:   can just append to memo to make simpler
        '''
        words = set(wordDict)
        memo = [-1]
        
        for i in range(len(s)):
            for j in memo:
                if s[j+1:i+1] in words:
                    memo.append(i)
                    break
        
        return memo[-1] == len(s)-1