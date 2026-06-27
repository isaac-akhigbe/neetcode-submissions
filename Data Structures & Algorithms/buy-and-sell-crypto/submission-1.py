class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0
        l, r = 0, 1

        while r < len(prices):
            maxp = max(maxp, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l += 1
            else:
                r += 1
        return maxp
        