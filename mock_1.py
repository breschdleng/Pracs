# Given a series such as 4, 4, 1, 3, 2, 2 print the output such as 11221324.
# ou free to use any programming language of your choice
##arr = [2,4,7,7,8,8] outpüut= 12142728
## arr = None
## arr > 0, for eg. [2,4,7,7,8,8]
## arr[i] < 0 eg. [2,-2,-2,4,5,5]
## arr[i] ==  num  eg arr = [9,9,9,9,9] output = 59


# step 1) handle when array is null
# step 2) create a dictionary
# step 3) iterate through the array, and check the each element of the array with the dictionary
# step 4) if elemen not in dictionary add the element and update the value by 1
# step 5) if elemen is already present then update the dictionary by 1
# step 6) sort the array ,arr_sort
# step 7) iterate arr_sort look up arr_sort and retrive dict value and print element dictionary freq, array_sort element


def return_array_freq(arr):
    if len(arr) == 0:
        return None

    freq = {}

    for i in range(len(arr)):
        if (arr[i] not in freq):
            freq[arr[i]] = 1

        else:
            freq[arr[i]] += 1

    arr_sort = sorted(set(arr))

    print(arr_sort)

    string_for_print = ""

    for i in range(0, len(arr_sort)):
        string_for_print += str(freq[arr_sort[i]]) + str(arr_sort[i])
        last_element = arr_sort[i]

    print(string_for_print)


if __name__ == "__main__":
    arr = [-1, 4, 4, 1, 3, 2, 2]
    return_array_freq(arr)