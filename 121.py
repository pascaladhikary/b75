class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        notes:  follow up until dips below min
        '''
        profit = 0
        b = prices[0]
        
        for i, p in enumerate(prices):
            profit = max(profit, p-b)
            if p < b:
                b = p
        
        return profit
            