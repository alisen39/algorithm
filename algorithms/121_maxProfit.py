#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/28 20:15
# desc:
""" 121. 买卖股票的最佳时机
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profile = 0
        for price in prices[1:]:
            profile = price - min_price
            if profile > max_profile:
                max_profile = profile
            if price < min_price:
                min_price = price
        return max_profile


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3]))
