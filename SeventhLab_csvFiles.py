from collections import Counter
from re import sub
import csv


def word_count(filepath):
    with open(filepath) as f:
        text = f.read()
        text = text.lower()  # open file and convert all letters into lowercase
    text = sub(r'[^a-zA-Z \n]', '', text)  # remove all non-words
    count_dict = Counter(text.split())  # count words
    result_lst = [(k, v) for k, v in count_dict.items()]
    return result_lst  # result dictionary as list of words and their number


with open("word_count.csv", "w", newline='') as csvfile:
    # open file for writing. newline '' is for writing without blank rows.
    writer = csv.writer(csvfile, delimiter='-')
    for pair in word_count("Homework5.txt"):
        writer.writerow([pair[0], pair[1]])  # write a word with number using
        #delimiter -


def letters(filepath):  # function to get a list of all
    # different letters in file
    with open(filepath) as f:
        text = f.read()
    text = sub(r'[^a-zA-Z]', '', text)
    count_dict = Counter(text)
    list_of_letters = [k for k, v in count_dict.items()]
    return list_of_letters


def letter_count(filepath):
    with open(filepath) as f:
        text = f.read()
    text = sub(r'[^a-zA-Z]', '', text)
    count_dict = Counter(text)
    result_lst = [(k, v) for k, v in count_dict.items()]

    sum_of_letters = 0  # this is for counting percentage
    for elem in result_lst:
        sum_of_letters += elem[1]

    list_of_dicts = list()
    for i in result_lst:
        if i[0].islower():  # if letter is lowercase
            dict_item = {'letter': i[0], 'count_all': i[1], 'count_uppercase': 0}
            # create dictionary with values
            if i[0].upper() in letters(filepath):
                # if the same letter in uppercase in the list
                for j in result_lst:
                    if j[0] == i[0].upper():  # then values will be changed
                        dict_item['count_all'] += j[1]
                        dict_item['count_uppercase'] += j[1]
        else:  # if letter is uppercase
            dict_item = {'letter': i[0].lower(), 'count_all': i[1],
                         'count_uppercase': i[1]}
            # create dictionary with values
            if i[0].lower() in letters(filepath):
                # if the same letter in lowercase in the list
                for j in result_lst:
                    if j[0] == i[0].lower():  # then values will be changed
                        dict_item['count_all'] += j[1]
        list_of_dicts.append(dict_item)
    for dct in list_of_dicts:  # now we can count a percentage
        dct['percentage'] = round(100 * dct['count_all'] / sum_of_letters, 2)
    unique_dict = [k for j, k in enumerate(list_of_dicts)
                   if k not in list_of_dicts[j + 1:]]
    # just to remove duplicates
    return unique_dict


with open('letter_count.csv', 'w', newline='') as csvfile:
    header = ['letter', 'count_all', 'count_uppercase', 'percentage']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()  # write specific headers
    for i in letter_count("Homework5.txt"):
        writer.writerow(i)  # add all counted values to csv file
