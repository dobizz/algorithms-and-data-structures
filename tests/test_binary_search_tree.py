#!/usr/bin/python3
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from binary_search_tree import Node, BST


def test_bst():
    arr = [3,5,2,1,4,6,7]

    bst  = BST(arr)

    # check if bst is not null
    assert bst is not None

    # check for bst depth
    assert bst.height == 3

    # check if all elements in bst
    for node in arr:
        assert node in bst

    # check if element not in bst
    assert max(arr) + 1 not in bst

    # check max value
    assert max(arr) == bst.max

    # check min value
    assert min(arr) == bst.min


if __name__ == '__main__':
    test_bst()