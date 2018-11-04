"""given two sorted linked lists merge them into one list
    solution: construct bst from the first list and insert second list into the first
    TC: mlog(n), where m is the num of elements of b and n is len(a)"""

import numpy as np
from  find_using_binary_search import Node, BinarySearchTree


def insert_nodes(root,value):

    #first process left sub-tree


    if value < root.value:
        if(root.left!=None):
            return insert_nodes(root.left,value)
        elif value < root.value:
            root.left = Node(value)
            return root.left
        elif value > root.value:
            root.right = Node(value)
            return root.right
    else:
        if (root.right != None):
            return insert_nodes(root.right, value)
        elif value < root.value:
            root.left = Node(value)
            return root.left
        elif value > root.value:
            root.right = Node(value)
            return root.right


def merge_lists(a, b):
    pass

if __name__ == '__main__':
    a = np.arange(1,20,2).tolist()
    bst = BinarySearchTree()
    root = bst.construct_bst("bst",a)
    print(root.value)
    b = np.arange(10,17,3).tolist()
    print(a,b)
    for i in range(len(b)):
        root_inserted = insert_nodes(root,b[i])

    print(bst.in_order_traversal("in_order",root))
