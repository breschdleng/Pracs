"""
construct a Binary Search Tree from a sorterd array or linked list using recursion
"""



def find_missing_element(root):
    """given a binary search tree find a missing element"""

    #do an in-order traversal given a binary tree

    print(in_order_traversal(root))
    found_element = -1

    return found_element

class Node:

    def __init__(self,value):

        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.num_levels = None

    def construct_bst(self, str,arr):

        if len(arr)==0:
            print(arr,"empty")
            return None

        mid_index = int(len(arr)/2)

        node = Node(arr[mid_index])

        node.left = self.construct_bst("process left",arr[:mid_index])

        node.right = self.construct_bst("process right",arr[mid_index+1:])

        return node

    def in_order_traversal(self,str, root):

        """ visit left, root and right sub-trees"""
        if (root.left != None):
            self.in_order_traversal("L", root.left)

        print(root.value)

        if (root.right != None):
            self.in_order_traversal("R", root.right)

    def pre_order_traversal(self, str, root):
        """ visit root, left and right sub-trees"""

        # print root value
        if (root != None):
            print(root.value)

        # then left sub-tree
        if (root.left != None):
            self.pre_order_traversal("L", root.left)

        # then right sub-tree
        if (root.right != None):
            self.pre_order_traversal("R", root.right)

    def level_order_traversal(self, str, root):
        """ visit root, left and right sub-trees"""

        # print root value
        if (root != None):
            print(root.value)

        # then left sub-tree
        if (root.left != None):
            self.pre_order_traversal("L", root.left)

        # then right sub-tree
        if (root.right != None):
            self.pre_order_traversal("R", root.right)

    def post_order_traversal(self, str, root):
        """ visit root, left and right sub-trees"""

        # left sub-tree
        if (root.left != None):
            self.post_order_traversal("L", root.left)

        # then right sub-tree
        if (root.right != None):
            self.post_order_traversal("R", root.right)

        # print root value
        if (root != None):
            print(root.value)

if __name__ == '__main__':

    arr = [1,2,4,5,7,30,40,55,70,100]
    print(arr)
    bst = BinarySearchTree()
    root = bst.construct_bst("start",arr)


    print("###########")
    print(root.value)
    print(root.left.value)
    print(root.left.left.value)
    print(root.right.right.value)

    print("in-order-traversal")

    bst.in_order_traversal("in-order", root)
    print("pre-order-traversal")
    bst.pre_order_traversal("pre-order", root)
    print("post-order-traversal")
    bst.post_order_traversal("post-order", root)

    #find_missing_element(root)
    #find missing element


