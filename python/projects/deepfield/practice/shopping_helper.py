#!/usr/bin/env python2.7
# coding=utf-8
"""Jerod Gawne, 2018.06.27

Shopping Helper (Myticas Coding Test)

Given a list of store inventories and a shopping list, return the minimum number of
store visits required to satisfy the shopping list.

For example, given the following stores & shopping list:

  Shopping List: 10 apples, 4 pears, 3 avocados, 1 peach

  Kroger: 4 apples, 5 pears, 10 peaches
  CostCo: 3 oranges, 4 apples, 4 pears, 3 avocados
  ALDI: 1 avocado, 10 apples
  Meijer: 2 apples

The minimum number of stores to satisfy this shopping list would be 3:
Kroger, CostCo and ALDI.
or
Kroger, CostCo and Meijer.

Usage: shopping_helper.py (shopping_list.json) (inventories.json)
"""
from __future__ import print_function, unicode_literals

import argparse
import itertools
import json


# todo: Should 'organic apples' count as apples or are these separate items?
#   - The code differentiates between the two, however given the
#     provided inventories it would be possible to reduce the stores
#     needed if they were counted as the same.

# note: I took some liberties with organization and structure in order to reduce complexity.
# note: I added sort to both the whole list as well as each combination.
# note: This could be simplified even further if written in python3.


def satisfy_shopping_list(shopping_list, inventory):
    """Jerod Gawne, 2018.06.27

    :param shopping_list:
    :param inventory:
    :return: None
    """
    store_inventories = {i: set() for i in shopping_list}

    for store in inventory['stores']:
        for item, quantity in store['inventory'].items():
            for k, v in shopping_list.items():
                if item == k and quantity >= v:
                    store_inventories[item].add(store['name'])

    stores_with_list_items = [list(v) for k, v in store_inventories.items()]
    store_permutations = [list(set(_)) for _ in list(itertools.product(*stores_with_list_items))]

    minimum = min(len(_) for _ in store_permutations)

    print("The shopping list can be satisfied by visiting a minimum of {} store(s):".format(minimum))
    [print(_) for _ in
     sorted(set([', '.join(sorted(stores, key=lambda s: s.lower())) for stores in store_permutations if len(stores) <= minimum]))]


if __name__ == '__main__':
    try:
        p = argparse.ArgumentParser()
        p.add_argument('--shopping_list_json_path', default='./shopping_list.json')
        p.add_argument('--inventory_json_path', default='./inventories.json')
        args = p.parse_args()

        with open(args.shopping_list_json_path) as shopping_list_json_file:
            shopping_list_json = json.load(shopping_list_json_file)

        with open(args.inventory_json_path) as inventory_json_file:
            inventory_json = json.load(inventory_json_file)

        satisfy_shopping_list(shopping_list_json, inventory_json)
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
