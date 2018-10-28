"""
Given a string, reverse the words of string
Example:
String: "This is a string"
Output: 'sihT', 'si', 'a', 'gnirts'
"""

def reverse_words(string):
    str_len = len(string[0])
    reversed = []

    print(string[0])
    k = 0
    #recover the string in a list using spaces as delimiter
    for i in range(str_len):
        if(string[0][i] ==" "):

            reversed.append(string[0][k:i])
            #skip the space
            k = i+1
        elif (i==str_len-1):
            reversed.append(string[0][k:i+1])

    for j in range(len(reversed)):
        print(reversed[j])
        reversed[j]=reversed[j][::-1]

    return reversed

if __name__ == '__main__':
    string = ["This is a string"]
    string_copy = string.copy()

    reversed = reverse_words(string_copy)

    print(reversed)