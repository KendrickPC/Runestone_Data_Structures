# # -*- coding: utf-8 -*-
# List Comprehension


def no_duplicates():
    word_list = ['cat','dog','rabbit']
    letter_list = []
    for a_word in word_list:
        for a_letter in a_word:
            letter_list.append(a_letter)
    # print(letterlist)

    # No duplicates
    # https://www.w3schools.com/python/python_howto_remove_duplicates.asp

    # Convert list to dictionary (no duplicates allowed in dictionary).
    # Convert dictionary back into a list.
    letter_list = list(dict.fromkeys(letter_list))
    print(letter_list)

no_duplicates()
