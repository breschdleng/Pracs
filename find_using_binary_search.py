"""
construct a Binary Search Tree from a sorterd array or linked list
"""

def find_element(arr):
    found_num_index = -1

    return found_num_index


class Node:

    def __init__(self,value):

        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.num_levels = None

    def construct_bst(self, arr):

        if len(arr)==0:
            print(arr)
            return None

        if(len(arr)!=0):
            mid_index = int(len(arr)/2)
            print(arr,mid_index)
            node = Node(arr[mid_index])

        if(len(arr[:mid_index])!=0 and len(arr[mid_index+1:])!=0):
            node.left = self.construct_bst(arr[:mid_index])
            node.right = self.construct_bst(arr[mid_index+1:])

        return node

if __name__ == '__main__':

    arr = [1,2,4,5,7,30,40,55,70,100]
    bst = BinarySearchTree()
    root = bst.construct_bst(arr)

    print(root.value)
    print(root.left.value)
    print(root.right.value)
    print(root.right.right.value)
    #prints 5
