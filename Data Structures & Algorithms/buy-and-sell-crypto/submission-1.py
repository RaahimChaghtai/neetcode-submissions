class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # BRUTE FORCE - TIME: O(n^2)
        # # Track the maximum profit found so far (initialized to negative infinity)
        # max_profit = float('-inf')
        
        # # Outer loop: Iterate through each price as the potential 'BUY' day
        # for i in range(len(prices)):
        #     # Inner loop: Iterate through remaining prices as potential 'SELL' days (must occur after buying)
        #     for j in range(i + 1, len(prices)):
        #         # Calculate profit if bought at day 'i' and sold at day 'j'
        #         profit = prices[j] - prices[i]

        #         # Only update max_profit if this transaction yields a positive gain
        #         if profit > 0:
        #             max_profit = max(profit, max_profit)
        
        # # Return the best profit if a profitable trade was found
        # if max_profit > float('-inf'):
        #     return max_profit
        # return 0


        # EFFICIENT - TIME: O(n)
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit
