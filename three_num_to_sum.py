# Given an array of numbers and a target sum. Find three numbers that can be added that results in the target
# a = [ 4, 2, 2, -1, 1, 0, 8, 4, 5, 4, 24, 7]
# target = 8
# output 4, 2, 2
# 7,1,0
# 5, 2, 1
# 7,2,-1
# 8,1,-1
# 4,5,-1

# Steps 1: check arr empty and return None with error, else Step 2
# Step 2: sort the array ascending order
# Step 3: take the first element of the array eg. -1 and subtract from target = 7
# Step 4: look at the mid element check if mid_elem < 7 or> 7, take 7 and subtract 8-7+1 = 2, search for 2
# Step 5: if mid_elem[first_half] if less than 2 search in mid_elem[second_half], if less look between mid_elem[second_half] and mid_elem[second_half], if 2 is found, add -1 7 and 2
# Step 6: start with second element, and so on.
# Step 7: result list hold the result

import numpy as np

def find_num_recur(arr, s, st, e):

    mid = int((st + e) / 2)

    if arr == None or mid < 0:
        return None

    mid_check = (mid > 0 or mid == 0) and mid < len(arr)-1

    if s > arr[mid] and mid_check:
        e -= 1
        return find_num_recur(arr,s,st,e)

    elif s < arr[mid] and mid_check:
        st += 1
        return find_num_recur(arr, s, st, e)
    elif s == arr[mid] and mid_check:
        return True
    else:
        return None


def recursive_variant(arr, target):

    length = len(arr)

    arr = sorted(arr)
    result = []

    for i in range(length):

        a = target - np.abs(arr[i])

        for j in range(i + 1, len(arr) - 1):
            s = a - arr[j]
            st = 0
            e = len(arr)-1

            if(find_num_recur(arr,s,st,e)):
                result.append((arr[i],arr[j],s))
    return result


def find_three_nos_to_sum(arr, target):

    if arr == None:
        return None

    length = len(arr)

    arr = sorted(arr)
    result = []

    for i in range(length):

        a = target -np.abs(arr[i])

        for j in range(i+1,len(arr)-1):


            search_no_2 = a - arr[j]

            start = 0
            end = len(arr)-1

            while (end > start):

                mid = int((start + end) / 2)

                if search_no_2 > arr[mid]:
                    end -=1

                elif search_no_2 < arr[mid]:
                    start +=1

                elif search_no_2 == arr[mid]:
                    number = search_no_2

                    result.append((arr[i],arr[j],number))

                    end = start

    return result

if __name__ == '__main__':

    arr=[2,1,4,5,7,2]
    target = 8

    #Solution 1:
    found_sol_1 = find_three_nos_to_sum(arr, target)


   #Solution 2:
    found_recur = recursive_variant(arr, target)
    unique_elem_1 = set(found_sol_1)
    unique_elem_2 = set(found_recur)
    print("solution 1",unique_elem_1)
    print("solution using recursion",unique_elem_2)