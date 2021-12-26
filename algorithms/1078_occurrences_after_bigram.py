#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/12/26 下午4:35
# desc:
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ret = []
        tag = text.split(' ')
        for i in range(len(tag) - 2):
            tmp = tag[i:i + 3]
            if first == tmp[0] and second == tmp[1]:
                ret.append(tmp[2])
        return ret


if __name__ == '__main__':
    # text = "alice is a good girl she is a good student"
    # first = "a"
    # second = "good"
    text = "we will we will rock you"
    first = "we"
    second = "will"
    r = Solution().findOcurrences(text, first, second)
    print(r)
