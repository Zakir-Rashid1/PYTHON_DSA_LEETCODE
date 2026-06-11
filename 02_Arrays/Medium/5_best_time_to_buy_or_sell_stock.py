

'''
Problem Statement: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def best_time_to_buy_sell_stock_1(prices):
    max_profit = 0 #Lowerbound of max_profit is 0 : according to the problem

    for i in range(len(prices)):
        buy_day = i #The day when i buyed the stock

        for j in range(i + 1, len(prices)):
            sell_day = j # The day when i sold the stock

            #Calculate the profit
            profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, profit) #Store maximum profit


    return max_profit


prices =  [3,3,5,0,0,3,1,4]
print(f"Maximum profit booked is: {best_time_to_buy_sell_stock_1(prices)}")




#Approach 02: Using Observation
#Time Complexity: O(n)
#Space Complexity: O(1)
def best_time_to_buy_sell_stock_2(prices):

    max_profit = 0 # Stores maximum profit found so far
    min_price = prices[0] # Minimum stock price seen so far

    for i in range(1, len(prices)):
        current_price = prices[i]

        current_profit = current_price - min_price # Profit if stock is sold today
        
        # Update maximum profit and minimum buying price
        max_profit = max(max_profit, current_profit) 
        min_price = min(min_price, current_price)

    return max_profit
        
    

prices =  [7,1,5,3,6,4]
print(f"Maximum profit booked is: {best_time_to_buy_sell_stock_2(prices)}")



