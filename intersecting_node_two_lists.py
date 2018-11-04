"""intersecting node between two linked lists"""

import numpy as np


def find_intersection(a,b):
    """
    append both the lists and construct a histogram, if the hist count > 1 and the element is seen thts the intersecting
    element
    TC: O(n+m)
    SC: O(n+m)
    """
    intersec_node = -1

    np_b = np.array(b)
    np_a = np.array(a)
    np_c = np.hstack((np_a,np_b))
    max_val = np.max(np_c)
    print(np_c)
    hist = np.zeros(max_val+1,dtype=int)
    for i in range(0,np_c.shape[0]-1):

        hist[np_c[i]] +=1

        if hist[np_c[i]] > 1:
            intersec_node = np_c[i]
            return intersec_node

    return intersec_node

if __name__ == '__main__':
    a = np.arange(1,10,1).tolist()
    del a[4:7]
    b = np.arange(5, 10, 1).tolist()

    print(a,b)
    print(find_intersection(a,b))