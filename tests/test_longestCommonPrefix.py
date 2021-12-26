#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-11-21 23:00
from unittest import TestCase

from algorithms import longestCommonPrefix

class TestSolution(TestCase):

    def test_longestCommonPrefix(self):
        longestCommonPrefix.Solution().longestCommonPrefix(['abc','abcdefg','bc'])
        self.fail()
