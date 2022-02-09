# from library "random" import
# function "randint" to get random integer in range
# function "sample" to get different list of values without repetitions
from random import randint, sample
# from library "string" import
# function "ascii_lowercase" to get all ascii lowercase symbols
from string import ascii_lowercase
# from library "pprint"
# import function "pprint" to get more readable results
from pprint import pprint

number_of_dicts = randint(2, 10)  # random number of dictionaries


# print(number_of_dicts)
# print(number_of_letters)


def generate_one_dict():
    """
    Function to generate one dictionary with specified
    number of letters
    :return: dictionary where key = unique letter,
    value = random integer value from 0 to 100
    """
    number_of_letters = randint(2, 26)  # random number of letters
    # I used only lowercase latin (to be honest only English) symbols,
    # so they are only 26
    new_dict = dict() # create empty dictionary
    # set list of letters with random length of numbers
    letter_choices = sample(ascii_lowercase, k=number_of_letters)
    for i in letter_choices:
        new_dict[i] = randint(0, 100) # add random value for each letter
    return new_dict # return filled dictionary


# create list of dicts using function generate_one_dict
all_dicts = [generate_one_dict() for i in range(number_of_dicts)]

pprint(all_dicts) # to check input dictionaries
# my test dictionary
'''
test_all_dicts = [{'b': 10, 'c': 4, 'n': 3, 'p': 7, 'r': 3, 'w': 10},
 {'b': 5, 'c': 6, 'f': 4, 'u': 6, 'v': 8, 'z': 6},
 {'e': 10, 'g': 0, 'o': 7, 's': 5, 't': 1, 'x': 6},
 {'a': 9, 'c': 0, 'd': 7, 'n': 5, 'o': 6, 'v': 8},
 {'b': 2, 'f': 8, 'h': 3, 'j': 3, 'p': 8, 'r': 8}]
'''


def unite_all_numbers(lst_of_dicts: list):
    """
    Function is created to unite all keys and their according
    values into one huge dictionary.
    If there aren't key in some dictionaries - value '-1' will be
    populated.
    :param lst_of_dicts: this is the list of generated dictionaries
    :return: dictionary with values that will be as
    a list with numbers (e.g., 'b': [10, 5, -1, -1, 2])
    """
    all_numbers = dict()  # create empty dictionary
    # find all unique keys from all dictionaries
    all_keys = [x for d in lst_of_dicts for x in d.keys()]
    for i in all_keys:
        # create corresponding empty list for each key
        all_numbers[i] = list()
    for dic in lst_of_dicts:
        for key in all_numbers:
            if key in dic:  # if key is in current dictionary
                # add value to list
                all_numbers[key].append(dic[key])
            else:  # if key isn't in current dictionary
                # add -1 value to list
                all_numbers[key].append(-1)
    return all_numbers  # return filled dictionary with list of values


unit_dict = unite_all_numbers(all_dicts)
# unit_dict = unite_all_numbers(test_all_dicts)


def max_num_and_index(lst: list):
    """
    Function is created to get maximum value and its index
    to set them into result dictionary.
    If there is only one positive value, then index = -1
    :param lst: list of values for some key
    :return: a tuple, tuple[0] = maximum value,
    tuple[1] = index of maximum value
    """
    if len([i for i in lst if i >= 0]) == 1:
        return max(lst), -1  # return tuple with maximum value and index = -1
    # else return maximum value and its index+1 (to get real index)
    return max(lst), lst.index(max(lst)) + 1


result_dict = dict()  # creation an empty final dictionary

for i in unit_dict:  # loop for each key from dictionaries
    # if there is only one positive value, the index == -1 and
    # then key will not be changed
    if max_num_and_index(unit_dict[i])[1] == -1:
        result_dict[i] = max_num_and_index(unit_dict[i])[0]
    # else if there is more that one positive values,
    # then key should be renamed
    else:
        result_dict[f'{i}_{max_num_and_index(unit_dict[i])[1]}'] \
            = max_num_and_index(unit_dict[i])[0]

print("Result dict: ", result_dict)  # print final dictionary

