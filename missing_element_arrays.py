"""Given two integer arrays where second array is duplicate of first array with just 1 element missing. Find the element.
Example:

Input:
Array1 - 9 7 8 5 4 6 2 3 1
Array2 - 2 4 3 9 1 8 5 6

Output:
7
"""

import numpy as np

"""solution 1: sum both arrays and take diff between them"""
def missing_element_sol_1(a,b):

    a_arr = np.array(a, dtype = int)
    b_arr = np.array(b, dtype=int)

    sum_a = np.sum(a_arr,axis=0)
    sum_b = np.sum(b_arr, axis=0)

    return np.abs(sum_b-sum_a)


"""solution 2: contatenate both arrays and take freq of them"""
def missing_element_sol_2(a,b):

    a_arr = np.array(a, dtype = int)
    b_arr = np.array(b, dtype=int)

    concat = np.hstack((a_arr,b_arr))
    print(concat)
    hist = np.zeros(concat.shape[0])

    for i in range(concat.shape[0]):
        hist[concat[i]] +=1

    missing_element = np.nonzero(hist == 1)
    return  missing_element [0][0]


if __name__ == "__main__":

    a = [9, 7, 8, 5, 4, 6, 2, 3, 1]
    b = [2, 4, 3, 9, 1, 8, 5, 6]

    print(missing_element_sol_2(a,b))




