# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

prices = [7,1,5,3,6,4]

def maxProfit(prices):
    profit = 0
    buy = prices[0]
    for sell in prices:
        if sell < buy:
            buy  = sell
        if profit < (sell - buy):
            profit  = sell - buy
    return profit

print(maxProfit(prices))