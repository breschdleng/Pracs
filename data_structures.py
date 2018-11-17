"""implements queue and stack data structures"""

import numpy as np
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

"""stack implementation
        LIFO"""
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):

        return self.size

    def is_empty(self):
        """is the stack empty"""
        if self.head == None:
            return True
        else:
            return False

    def push(self,value):
        """insert_node"""

        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            self.size +=1
        else:
            node = Node(value)
            temp = self.head
            node.next = temp
            self.head = node
            self.size += 1


    def pop(self):

        temp = self.head

        self.head = self.head.next
        self.size -=1


        return temp.value

    def peek(self):

        return self.head.value

    def insert(self,index, value):

        temp = self.head
        node = Node(value)
        if index == 0:

            node.next = self.head
            self.head = node

        elif index == self.size-1:
            temp2 = self.tail
            self.tail = node
            temp2.next = self.tail

        else:
            for i in range(0,index-1):
                temp = temp.next

            temp2 = temp.next
            temp.next = node
            node.next = temp2
        self.size +=1


    def delete(self,index):

        temp = self.head

        if index < 0 or index > self.size-1:
            print("index out of array bounds")
            return None

        if index == 0:
            self.head = temp.next
            print("deleting", temp.value)
        else:
            for i in range(0,index-1):
                temp = temp.next

            print("deleting", temp.next.value)
            temp.next = temp.next.next

            if index == self.size-1:
                self.tail = temp.next

        self.size -=1


    def print_stack(self):

        node = self.head
        for i in range(self.size):
            print(node.value)
            node = node.next


"""queue implementation
        FIFO"""
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):

        return self.size

    def is_empty(self):
        """is the stack empty"""
        if self.head == None:
            return True
        else:
            return False

    def en_queue(self,value):
        """insert_node"""
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = self.head
            self.size +=1
        else:

            temp = self.tail
            temp.next = node
            self.tail = node

            self.size += 1


    def de_queue(self):

        temp = self.tail
        self.tail = self.tail.next

        self.size -=1

        return temp.value

    def peek(self):

        return self.tail.value

    def print_stack(self):

        node = self.head
        for i in range(self.size):
            print(node.value)
            node = node.next

if __name__ == '__main__':

    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(40)
    stack.push(70)

    stack.push(-1)
    stack.push(-6)
    stack.push(-9)

    print("orig")
    stack.print_stack()
    val1 = stack.pop()
    val2 = stack.pop()

    val3 = stack.pop()
    val4 = stack.pop()


    print("popping", val1, val2, val3, val4)
    #stack.insert(4,-90)

    stack.print_stack()


    print("Queue")

    q = Queue()
    q.en_queue(10)
    q.en_queue(20)

    q.en_queue(4020)
    q.en_queue(2087)
    q.print_stack()
    val = q.de_queue()
    print("pop",val)

    q.print_stack()
