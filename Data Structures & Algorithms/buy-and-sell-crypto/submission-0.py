class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We are looking for the max profit at two different in the array, buy low and sell high
        min_index = 0
        profit = 0

        for index, price in enumerate(prices):
            # if our current sell value - min value is greater than our previous profit, update
            if price > prices[min_index]:
                if (price - prices[min_index]) > profit:
                    profit = price - prices[min_index]
            # update the min value, if it is lesser than the previous one
            if price < prices[min_index]:
                min_index = index
        return profit

            
        