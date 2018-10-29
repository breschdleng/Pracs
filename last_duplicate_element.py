"""
We have a sorted array with duplicate elements and we have to find the index of last duplicate element
and print index of it and also print the duplicate element.
If no such element found print a message.

"""

"""
straightforward way 
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


def solution_2():
    return None

if __name__ == '__main__':

    a = [1,2,2,3,4,5,7,0,1]

    b = solution_1(a)
    print(b)





