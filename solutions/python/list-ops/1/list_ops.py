"""Exercism: List Ops"""


def append(list1, list2):
    """Combine two lists by placing all items of list2 after list1."""
    
    result = []

    for item in list1:
        result = [*result, item]

    for item in list2:
        result = [*result, item]

    return result

    
def concat(lists):
    """Combine a series of lists into a single flattened list."""
    
    flattened_list = []
    
    for list in lists:
        flattened_list = append(flattened_list, list)

    return flattened_list
    

def filter(function, list):
    """Filter items from a list based on a predicate function."""
    
    filtered_list = []

    for item in list:
        if function(item):
            filtered_list = [*filtered_list, item]

    return filtered_list


def length(list):
    """Return the total number of items within a list without using len()."""
    
    lists_lenght = 0

    for item in list:
        lists_lenght += 1

    return lists_lenght


def map(function, list):
    """Apply a function to all items of a list and return the results."""
    
    result = []

    for item in list:
        result = [*result, function(item)]

    return result


def foldl(function, list, initial):
    """Fold each item into the accumulator from left to right."""
    
    for item in list:
        initial = function(initial, item)

    return initial


def reverse(list):

    reversed_list = []

    for item in list:
        reversed_list = [item, *reversed_list]

    return reversed_list

def foldr(function, list, initial):

    for item in reverse(list):
        initial = function(initial, item)

    return initial
