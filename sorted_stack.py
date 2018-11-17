from data_structures import Stack

def sort_stack():

    a = Stack()
    a.push(-1)
    a.push(7)
    a.push(3)
    a.push(2)
    a.push(10)

    n = 5

    b = Stack()

    i = n

    for j in range(n):
        i = n
        b_filled = False
        while(i>0):

            if (b_filled == False):
                b.push(a.pop())
                b_filled = True
                i-=1

            f = a.peek()
            s = b.peek()
            if(f < s):
                temp = b.pop()
                b.push(a.pop())
                i -= 1
                b.push(temp)
            else:
                b.push(a.pop())
                i -= 1
        k = n
        while(k > 0):
            num = b.pop()
            a.push(num)
            k -= 1

    a.print_stack()

if __name__ == '__main__':

    sort_stack()
