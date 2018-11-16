



class Node:

    def __init__(self, ar):
        self.left = None
        self.right = None
        self.ar = ar

class Tree:
    def __init__(self):
        self.root = None

    def Create(self, ar):


        mid = int(len(ar) / 2)

        node = Node(ar)

        if len(ar) < 2:
            return node

        node.left = self.Create(ar[:mid])
        node.right = self.Create(ar[mid:])

        node = self.merge(node)

        return node

    def merge(self, node):

        if node.left == None:
            a=[]
        else:
            a = node.left.ar

        if node.right==None:
            b = []
        else:
            b = node.right.ar


        l = len(a)
        r = len(b)
        c = len(node.ar)

        i = 0
        j = 0
        k = 0

        while(i < l and j < r):
            if a[i] <= b[j]:
                node.ar[k] = a[i]
                i +=1
            else:
                node.ar[k] = b[j]
                j +=1
            k +=1

        while(i < l):
            node.ar[k] = a[i]
            i += 1
            k += 1
        while (j < r):
            node.ar[k] = b[j]
            j += 1
            k += 1
        return node



if __name__ == '__main__':
    a = [4, 7, 2, 5, 1, 6]
    bt = Tree()
    root = bt.Create(a)
    print(root.ar)




