"""
We have a sorted array with duplicate elements and we have to find the index of last duplicate element
and print index of it and also print the duplicate element.
If no such element found print a message.

"""

"""
O(n)
"""
def solution_1(a):

    if(a == None):
        return "empty list given"

    list_len = len(a)
    last_element = 0
    last_repeating_element = -1
    last_index = -1

    last_element = a[0]
    for i in range(1,list_len):
        if a[i] == last_element:
            last_repeating_element = a[i]
            last_index = i

        last_element = a[i]

    if last_repeating_element == -1 and last_index == -1:
        return None
    else:
        return last_repeating_element, last_index


def solution_bfs(a, num):
    list_len = len(a)

    #check for even or odd
    if(list_len%2 == 0):
        half = int((list_len+1)/2)
    else:
        half = int(list_len/2)

        print(half)

    # todo incomplete
    for i in range(0,list_len):
        if(a[half] == num):
            return half
        elif num < a[half]:
            return solution_bfs(a[:half],num)
        elif num > a[half]:
            return solution_bfs(a[half:],num)


if __name__ == '__main__':

    a = [1,2,2,3,4,5,7]

    #O(n)
    b = solution_1(a)
    print(b)

    #O(nlogn)
    #not related to finding the last duplicate element but
    #good practice for binary search tree

    found_index = solution_bfs(a,5)
    print(found_index)





