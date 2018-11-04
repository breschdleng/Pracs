"""find missing number increasing sequence"""
import numpy as np



def find_missing_element_1(slice, arr):

    #do a binary search

    length = len(arr)
    mid_index = int((length-1)/2)
    #print(arr, arr[mid_index], mid_index, slice + mid_index, arr[mid_index]+1)

    if(length == 1):
        return arr[0]-1


    if arr[mid_index] == slice + mid_index:
        print(arr, arr[mid_index], mid_index, slice + mid_index, arr[mid_index] + 1)
        return find_missing_element_1(arr[mid_index]+1, arr[mid_index+1:])
    else:
        print(arr, arr[mid_index], mid_index, slice + mid_index, arr[mid_index] + 1)
        return find_missing_element_1(arr[0], arr[:mid_index + 1])



if __name__ == '__main__':

    arr = np.arange(0,32,1).tolist()
    del arr[26]

    miss_elem = find_missing_element_1(0,arr)
    print(miss_elem)

