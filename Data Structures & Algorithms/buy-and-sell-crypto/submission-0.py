class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float("inf")
        maxprofit= 0 
        profit=0
        for i in range (len(prices)):
            minprice=min(minprice,prices[i])
            if prices[i]> minprice:
                profit=prices[i]-minprice
                if maxprofit<profit:
                    maxprofit=profit
        return maxprofit
        