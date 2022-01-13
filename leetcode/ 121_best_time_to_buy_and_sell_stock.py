class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        while len(prices) > 1 :
            min_price, max_price = min(prices), max(prices)
            index_of_min = prices.index(min_price)
            index_of_max = prices.index(max_price)
            
            if index_of_min < index_of_max :
                return max_price - min_price
            else :
                prices.pop(index_of_max)
            
        return 0