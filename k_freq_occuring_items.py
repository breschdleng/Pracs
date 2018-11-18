# Given an array of numbers, return the top k repeated elements of the array
# a = [122233] output k = 2, 3,2 on the frequency

# a = [-1-122200]

# hist['-1'] = 2 --> hist['2'] = -1
# hist['2'] =  3
# hist['0'] =  2,--> hist['2'] = 0
# k = 2, [0, 2] or [-1,2]

# sort = 2,2,3
# a =[] k, output None

# Step 1) compute frequencies with a dictionary
# Step 2) take dictionary and k and sort the freq and output k corresponding key values


class Freq:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.size = None


def histogram(input_array, k):
    dictionary = {}

    for i in range(len(input_array)):
        if (input_array[i] not in dictionary):
            dictionary[input_array[i]] = 1
        else:
            dictionary[input_array[i]] += 1

    dic_to_list = []

    for i in range(len(input_array)):
        freq_elem = Freq(input_array[i], dictionary[input_array[i]])
        dic_to_list.append(freq_elem)

    for i in range(len(dic_to_list)):
        for j in range(len(dic_to_list) - 1):
            if dic_to_list[j].value > dic_to_list[j + 1].value:
                dic_to_list[j], dic_to_list[j + 1] = dic_to_list[j + 1], dic_to_list[j]

    for i in range(k):
        print(dic_to_list[i].key)


if __name__ == "__main__":
    input_arr = [1, 2, 2, 2, 0, 0]
    histogram(input_arr, 3)



