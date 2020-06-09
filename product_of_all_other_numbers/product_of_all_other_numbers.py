"""
Input: a List of integers
Returns: a List of integers
"""

"""
    Quick and dirty:
        Make a new list for returning the result
        iterate through given list:
            slice it around the curr position ( arr[:i] + arr[i+1:] )
            call math.prod
            assign it to res_list[i]
        return res_list
        
"""
from math import prod


def product_of_all_other_numbers(arr):
    res = [0] * len(arr)

    for i in range(0, len(arr)):
        res[i] = prod(arr[:i] + arr[i + 1 :])

    return res


if __name__ == "__main__":
    # Use the main function to test your implementation
    # arr = [90, 9]
    arr = [
        2,
        6,
        9,
        8,
        2,
        2,
        9,
        10,
        7,
        4,
        7,
        1,
        9,
        5,
        9,
        1,
        8,
        1,
        8,
        6,
        2,
        6,
        4,
        8,
        9,
        5,
        4,
        9,
        10,
        3,
        9,
        1,
        9,
        2,
        6,
        8,
        5,
        5,
        4,
        7,
        7,
        5,
        8,
        1,
        6,
        5,
        1,
        7,
        7,
        8,
    ]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}"
    )
