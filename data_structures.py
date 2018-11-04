"""implements queue and stack data structures"""

import numpy as np
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

"""stack implementation"""
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        self.size = 0

        if(self.head != None):
            node = self.head
            while(node != None):
                self.size +=1
                node = node.next
        return self.size

    def is_empty(self):
        """is the stack empty"""
        if self.head == None:
            return True
        else:
            return False

    def insert_node(self,value):
        """insert_node"""

        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            self.size +=1
        else:
            node = self.head
            while(node!= None):
                node =  node.next

            node = Node(value)
            self.size += 1

            self.tail = node

            node = self.head

            while(node.next!=None):
                node = node.next

            node.next = self.tail

    def pop(self):

        node = self.head

        while(node.next != None):
            node = node.next

        self.tail = node

        node_temp = self.head
        self.size -= 1

        for i in range(self.size):
            node_temp = node_temp.next

        node_temp = self.tail

        return node_temp.value

    def peek(self):
        pass

    def print_stack(self):

        node = self.head
        for i in range(self.size):
            print(node.value)
            node = node.next


"""queue implementation"""
class Queue:
    def __init__(self):
        self.list = None
        self.size = None

    def size(self):
        return len(self.list)

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def insert_node(self,value):
        pass

    def pop(self,value):
        pass

    def peek(self,value):
        pass


if __name__ == '__main__':

    stack = Stack()
    stack.insert_node(10)
    stack.insert_node(20)
    stack.insert_node(40)
    stack.insert_node(70)
    val = stack.pop()
    print("pop",val)
    print("stack size", stack.size)
    stack.print_stack()