class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        notes:  follow up until dips below min
        '''
        n = len(prices)
        min_val = prices[0]
        res = 0

        for i in range(n):
            res = max(res, prices[i]-min_val)

            if prices[i] < min_val:
                min_val = prices[i]
                        
        return res
            