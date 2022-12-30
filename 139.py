class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        notes:  sub problem: does a seq end at i
                hold end of each word as j in memo
                if [j:i] in words then add i+1
        crux:   can just append to memo to make simpler
        '''
        n = len(s)
        words = set(wordDict)
        memo = [0]

        for i in range(n):
            for j in memo:
                if s[j:i+1] in words:
                    memo.append(i+1)
                    break

        return memo[-1] == n