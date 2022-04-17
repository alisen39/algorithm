#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/12/27 下午8:20
# desc:
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        send_cnt = 0
        ages.sort()
        for x in range(len(ages)):
            if x > 120:
                continue
            for y in range(len(ages[:x])):
                if x == y:
                    continue
                if ages[y] > ages[x]:
                    break
                if ages[y] <= 0.5 * ages[x] + 7 or (ages[y] > 100 and ages[x] < 100):
                    continue
                send_cnt += 1
                # print(ages[x], ages[y])
        return send_cnt


if __name__ == '__main__':
    # ages = [16, 16]
    # ages = [16, 17, 18]
    ages = [20, 30, 100, 110, 120]
    res = Solution().numFriendRequests(ages)
    print(res)
