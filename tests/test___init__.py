#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/14 23:03
# desc:
from unittest import TestCase


from algorithms.utils.list_node import parse_list_node, gen_list_node, gen_tree_node


class Test(TestCase):
    def test_gen_tree_node(self):
        tree = gen_tree_node([1, 2, 3, 4])
        print(tree)

    def test_gen_list_node(self):
        list_node = gen_list_node([1, 2, 3, 4])
        print(list_node)

    def test_parse_list_node(self):
        list_node = gen_list_node([1, 2, 3, 4])
        print(list_node)

        arr = parse_list_node(list_node)
        print(arr)
