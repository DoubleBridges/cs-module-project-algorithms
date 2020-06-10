"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(nums, k):
    # Initialize a result list for storing max values
    # Set a pointer for the begining and end of the subarray being evaluated
    res_arr = []
    i = 0
    j = k
    # Set the max value for the first subarray
    # max_val = max(nums[i:j])
    # Increment begining and end pointers by 1
    # i += 1
    # j += 1
    # Iterate through the original array, if the newest val (k) is greater than mav_val
    #
    while i <= len(nums) - k:
        sub_array = nums[i:j]
        res_arr.append(max(sub_array))
        i += 1
        j += 1

    return res_arr


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
