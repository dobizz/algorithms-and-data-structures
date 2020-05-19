#!/usr/bin/python3
'''binary search'''
'''
[TODO]
    - Add delete from BST
    - Make BST balanced
    - Add show function or __str__ dunder method to print visualized tree in terminal
'''
from collections import deque


class Node:
    '''Binary Search Tree Node class'''

    def __init__(self, data):
        '''new node constructor'''
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return f'<{self.left}:{self.data}:{self.right}>'


class BST:
    '''Binary Search Tree class'''

    def __init__(self, arr: list=None):
        self.tree = None

        # create BST if input list is given
        if arr:
            root = None
            for data in arr:
                root = self.insert(root, data)

    def __repr__(self):
        return f'{self.tree}'

    def __contains__(self, value):
        return self.__search(value)

    def insert(self, root=None, data=None):
        '''insert new node in BST'''
        if root:
            if data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        else:
            return Node(data)

        self.tree = root

        return root

    @property
    def min(self):
        '''returns left most node'''
        node = self.tree

        while node.left is not None:
            node = node.left

        return node.data

    @property
    def max(self):
        '''returns right most node'''
        node = self.tree

        while node.right is not None:
            node = node.right

        return node.data

    @property
    def height(self):
        return self.__getHeight(self.tree)

    def __getHeight(self, root=None):
        '''return the maximum depth of the BST'''
        if root is None:
            return -1

        left = self.__getHeight(root.left)
        right = self.__getHeight(root.right)

        return 1 + max(left, right)

    def __search(self, value):
        q = deque()

        curr = self.tree

        # use BFS to search BST
        while curr is not None:
            if curr.data == value:
                return True

            left = curr.left
            right = curr.right

            if left:
                q.append(left)

            if right:
                q.append(right)

            # if queue is empty
            if not q:
                break

            # get items to check from queue
            curr = q.popleft()