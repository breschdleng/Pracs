"""
Given a dictionary of words and a string of characters, find if the string of characters can be broken into individual valid words from the dictionary.
Example:
Dictionary: arrays, dynamic, heaps, IDeserve, learn, learning, linked, list, platform, programming, stacks, trees
String    : IDeservelearningplatform
Output   : true
Because the string can be broken into valid words: IDeserve learning platform
https://www.geeksforgeeks.org/word-break-problem-dp-32/
https://www.ideserve.co.in/learn/word-break-problem
"""


import time


"""
searches the first character in the target string against the dictionary which outputs a  set of matched words.
These matched words are then checked on the target to check for a word match. If the word is matched 
the book keeping list is appended.
 
"""
def check_solution_2(target, dictionary):

    length_tar = len(target[0])
    char_tar = target[0]


    #contains the final solution
    book_keeping = []

    #contains all unique words that have a matching character with the characters in the target string
    matched_dictionary = []
    length_dict = len(dictionary)


    for tar_index in range(length_tar):
        for dict_index in range(length_dict):
            if char_tar[tar_index] == dictionary[dict_index][0]:
                if(dictionary[dict_index] not in matched_dictionary):
                    matched_dictionary.append(dictionary[dict_index])

    #found unique words in the dictionary that have a matching character with words in the string
    print("matched dictionary",matched_dictionary)

    for items in range(len(matched_dictionary)):
        if (target[0][:len(matched_dictionary[items])] == matched_dictionary[items]):
            book_keeping.append(target[0][:len(matched_dictionary[items])])
            target[0]=target[0][len(matched_dictionary[items]):]

    return book_keeping

if __name__ == '__main__':

    dictionary = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
                  'cream','cup', 'icecream', 'man', 'go', 'mango']

    target = ['creamcupmango']
    target_copy = target.copy()

    #check the starting character against the dictionary character and if present cut that length

    start_time = time.time()
    word_split = check_solution_2(target_copy,dictionary)
    end_time = time.time()
    print("word split",word_split)
    print("execution time is ",end_time-start_time)
    print("dictionary",dictionary)
    print("target string", target)

