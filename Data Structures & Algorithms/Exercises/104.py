#
# List: Max Profit
#
# You are given a list of integers representing stock prices for a certain
# company over a period of time, where each element in the list corresponds
# to the stock price for a specific day.
#
# You are allowed to buy one share of the stock on one day and sell it on a
# later day.
#
# Your task is to write a function called max_profit that takes the list of
# stock prices as input and returns the maximum profit you can make by buying
# and selling at the right time.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5850776
#


def max_profit(prices):
    min_price, max_profit = float("inf"), 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
