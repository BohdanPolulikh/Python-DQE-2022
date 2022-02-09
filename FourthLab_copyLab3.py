import re


def normalize_text(file: str):
    '''
    Task 1
    Function will remove all empty rows and
    capitalized first letter in each row.
    :param file: file with given text
    :return: result: text without extra spaces and empty rows.
    '''
    result = ''
    with open(file, encoding='utf8') as f:
        lines = f.readlines()  # lines is a list with each row
        for line in lines:  # for each row in list
            result += line.lstrip().capitalize()  # remove all spaces
            # before text, capitalize first word and add changed row
            # into result variable
    return result


def upper_first_letter_after_dot(s: str):
    '''
    Task 1 part 2.
    Function to capitalize first letter in all words after each dot
    :param s: given text
    :return: the same text, but with upper letters
    '''
    return re.sub("(^|[.?!])\s*([a-zA-Z])", lambda p: p.group().upper(), s)
    # find all matches to reg expression (any letter after . or ! or ?) and
    # upper this letter.


def sentence_with_last_words(s: str):
    '''
    Task 2 part 1
    Function to collect all last words from each sentence
    in the text and create new sentence with them
    :param s: text
    :return: sentence with
    '''
    last_words = [i[:-1] for i in re.findall(r'[\w\d]+\.', s)]
    # findall will find all words that ends with dot = last word in text s
    # we will add all words without last symbol, because last symbol = dot
    # and return sentence with all found words separated by comma
    return f"This is the sentence with words: {', '.join(last_words)}."


def add_sentence_after_paragraph(text: str, sentence: str):
    """
    Task 2 part 2
    Function to add new sentence into text after word 'paragraph'
    :param text: given text
    :param sentence: sentence to add
    :return: text with new new sentence
    """
    return text.replace('paragraph.', 'paragraph. '+sentence)


def change_iz(s: str):
    '''
    Task 3
    Function to change all misspeling words 'iz' on 'is'.
    :param s: text
    :return: text with changed words
    '''
    return s.replace(' iz ', ' is ')


def count_spaces(file: str):
    """
    Task 4
    Function is created to resolve task #1,
    to count all spaces in file with task text.
    :param file: file with given text
    :return: number of spaces
    """
    with open(file, encoding="utf8") as f:  # param 'enconding' has been
        # added to read file with symbol “
        x = f.read()  # open file and read it
    all_spaces = len(re.findall(r'\s', x))  # \s - is any space
    # findall - will create list with all found spaces in text 'x'
    return all_spaces


# call all defined functions
normalized_text = upper_first_letter_after_dot(normalize_text('Homework3.txt'))
print("Task 1.")
print(normalized_text)
print("\nTask 2.")
new_sentence = sentence_with_last_words(normalized_text)
print(add_sentence_after_paragraph(normalized_text, new_sentence))
print("\nTask 3.")
print(change_iz(normalized_text))
print("\nTask 4.")
print(count_spaces("Homework3.txt"))
