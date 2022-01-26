from random import randint  # import function "randint" from library "random"

full_list = [randint(0, 1000) for i in range(100)]  # new list with 100 random numbers


def selection_sort(lst: list):
    """
    Steps in Selection sorting:
    1. Find index of minimal element
    2. Swap minimal and first elements (user receives Sorted 1-element list, other part is non-sorted)
    3. Find index of minimal element in the non-sorted list (started from element #2)
    4. Swap minimal and second element (user receives Sorted 2-elements list, other part is non-sorted)
    5. Check all elements
    :param lst: type list
    :return: sorted list
    """
    i = 0  # start point - is lst[0], the first element of the list
    while i < len(lst):  # to check all elements in the list
        min_elem = min(lst[i:])  # find minimal element in the non-sorted list
        index_of_min_elem = lst[i:].index(min_elem) + i  # find index of minimal element
        # operation (+i) - just for fixing list offset
        if i != index_of_min_elem:  # if current element is the least - pass this step
            lst[i], lst[index_of_min_elem] = lst[index_of_min_elem], lst[i]
            # else swap the current and minimal elements
        i += 1  # go to the next step
    return lst


def testing(lst: list):
    """
    Function is created to verify test results, without any additional info.
    :param lst:
    :return: if list is sorted correctly - then Passed, if sorted incorrectly - then Failed.
    """
    if lst == sorted(lst):
        print("Passed")
    else:
        print("Failed")


def is_even(x: int):
    """
    Function is created to check if the number is odd or even.
    :param x: integer number
    :return: if x is even - then True, if odd - False
    """
    return x % 2 == 0  # if x%2 = 0 then return True, else False


even_numbers = [i for i in full_list if is_even(i)]  # create list with only even numbers
odd_numbers = [i for i in full_list if not is_even(i)]  # create list with only odd numbers
sorted_list = selection_sort(full_list)
print(sorted_list)
# testing(sorted_list)


if len(even_numbers) == 0:  # check to avoid Zero Division
    print("There are no even numbers in the list")
else:
    evenAvg = sum(even_numbers) / len(even_numbers)
    print(f"Average of even numbers is {evenAvg}")
if len(odd_numbers) == 0:  # check to avoid Zero Division
    print("There are no odd numbers in the list")
else:
    oddAvg = sum(odd_numbers) / len(odd_numbers)
    print(f"Average of odd numbers is {oddAvg}")
