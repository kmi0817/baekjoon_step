class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices) :
            bigger_than_price = [x for x in prices[i+1:] if x > price]
            
            if bigger_than_price and max_profit < max(bigger_than_price) - price :
                max_profit = max(bigger_than_price) - price
                
        return max_profit