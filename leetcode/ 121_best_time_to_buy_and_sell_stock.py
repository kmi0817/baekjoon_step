class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price_i in enumerate(prices) :
            if i == len(prices) - 1 :
                break
            
            for j, price_j in enumerate(prices[i+1:]) :
                profit = price_j - price_i
                
                if profit < 0 :
                    break
                elif max_profit < profit :
                    max_profit = profit
                    
        return max_profit