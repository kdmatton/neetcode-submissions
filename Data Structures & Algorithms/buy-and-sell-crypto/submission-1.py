class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = minPrice = 0
        maxProfit = prices[maxPrice] - prices[minPrice]

        for i in range(1, len(prices)):
            if prices[i] < prices[minPrice]:
                minPrice = i
                maxPrice = i
            else: 
                maxPrice = i 
            
            currentProfit = prices[maxPrice] - prices[minPrice]
            maxProfit = max(maxProfit, currentProfit)
            
        return maxProfit