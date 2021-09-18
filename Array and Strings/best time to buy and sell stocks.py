'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

TC : O(n)
SP : O(1)
'''
def maxProfit(prices):
        start=0
        end=1
        price=0
        while(start<len(prices) and end<len(prices)):
            if(prices[start]>prices[end]):
                start+=1
                end+=1
            else:
                while(end<len(prices)-1 and prices[end]<prices[end+1]):
                    end+=1
                price+= (prices[end]-prices[start])
                start=end
                end+=1
                
                
        return price