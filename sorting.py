import numpy as np


def insert_sort(a):

    for i in range(len(a)):

        j = i
        while(j>0):

            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
            j-=1
    return a

def find_min_and_index(a, i):
    min = np.min(a, axis=0)
    idx = np.argmin(a)
    return min, idx+i

def selection_sort(a):
    for i in range(len(a)-1):
        min, idx = find_min_and_index(a[i+1:], i)

        if a[idx] < a[i]:
            a[i], a[idx] = a[idx], a[i]

    return a


if __name__ == '__main__':
    a = [4,7,2,5,1,6]

    print(insert_sort(a))
    print(selection_sort(a))
