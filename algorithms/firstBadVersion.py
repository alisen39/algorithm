#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-11-29 22:44

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
'''
第一个错误的版本
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/8/sorting-and-searching/53/

使用二分查找算法

'''


def isBadVersion(version):
    if version >= 6:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return n

        start = 1
        end = n
        while True:
            if start == end:
                break

            if isBadVersion(int((start+end)/2)):
                end = int((start+end)/2)
            else:
                start = int((start+end)/2)+1

        return start

if __name__ == '__main__':
    # version_count = 0
    # version_count = 1
    # version_count = 2
    # version_count = 5
    version_count = 10
    # version_count = 10000

    res = Solution().firstBadVersion(version_count)
    print(res)
