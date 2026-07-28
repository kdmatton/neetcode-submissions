class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = high = 0
        maxProfit = prices[high] - prices[low]

        for i in range(1, len(prices)):
            if prices[i] < prices[low]:
                low = i
                high = i
            if prices[i] > prices[high]:
                high = i 

            current = prices[high] - prices[low]
            maxProfit = max(current, maxProfit)

        return maxProfit