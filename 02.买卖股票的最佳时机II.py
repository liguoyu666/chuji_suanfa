# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 上午9:14
# @Author  : liguoyu
# @FileName: 02.买卖股票的最佳时机II.py
# @Software: PyCharm


# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
# 提示：
# 1 <= prices.length <= 3 * 10 ^ 4
# 0 <= prices[i] <= 10 ^ 4


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    profit = 0
    for i in range(0,len(prices)-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    return profit


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    y = maxProfit(prices)
    print(y)