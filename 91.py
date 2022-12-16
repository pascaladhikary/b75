class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        notes:  subproblem: num decodings at i
                we either add 1 width char taking (n-1) 
                or add 2 width char taking (n-2)
        crux:   need to add 1 to memo so memo[2] case can use prev 
        '''
        n = len(s)

        if s[0] == "0": return 0
        if n == 1: return 1

        memo = [0] * (n+1)
        memo[0] = 1
        memo[1] = 1

        for i in range(2, n+1):
            if s[i-1] != '0':
                if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7'):
                    memo[i] = memo[i-1] + memo[i-2]
                else:
                    memo[i] += memo[i-1]
            else:
                if s[i-2] == '1' or s[i-2] == '2':
                    memo[i] = memo[i-2]
                else:
                    return 0

        return memo[-1]