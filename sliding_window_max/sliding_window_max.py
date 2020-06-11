"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""

from collections import deque


def sliding_window_max(nums, k):
    """
    First Pass:

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
    """

    """
        To achieve O(n) time complexity, we can implement deque from the built in
        collections module. This is a double ended que, similar to a doubly linked list.
        Deque will allow us to add and remove elements from either end.
    """
    # Initialize a list for storing our max values
    res_arr = []
    # Initialize a deque for storing the indices of potetntial max values within our window
    max_que = deque()
    # Iterate through our list of nums, using enumerate to destructure the the index and value from each position in the list
    # Enumerate also helps with space complexity, since it is a generator and will give us one index, value pair at a time
    # Instead of holding the entire nums list in memory
    for (i, val) in enumerate(nums):
        # While the que is not empty, and the curr_val is greater than the value of the last index stored in the que
        # Remove the last value in the que
        # If the curr_val is larger than the val of any index in the que, it will empty the que
        while len(max_que) > 0 and val > nums[max_que[-1]]:
            max_que.pop()
        # Append the index of the curr-val to the que
        max_que.append(i)

        # j is the pointer for the left extent of our window, we use i and the passed window size to locate it
        # i is the pointer for the right extent of our window
        j = i + 1 - k
        # If the window is full (j >= 0), add the value of the index at the head of the que to our results list
        if j >= 0:
            res_arr.append(nums[max_que[0]])
            # If the the index of the max value and the left pointer are the same,
            # remove it from the head of the que, as it will be outside the window
            # on the next pass
            if j == max_que[0]:
                max_que.popleft()
    # Time complexity O(n), Space complexity O(n)
    return res_arr


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    #               j      i
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    #              mqh
    # max_que = [2,4]
    # res_arr = [3,3]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
