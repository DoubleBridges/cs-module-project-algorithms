"""
Input: an integer
Returns: an integer
"""


def eating_cookies(n):
    """ We know our base cases:
            0 = 1
            1 = 1
            2 = 2
            3 = 4
        So front load our base case values into an arr
        so that arr[base_case] = value
        Add (n - 3) elements to the initial arr for storing
        the calculated values
    """
    # Space complexity: O(n)
    arr = [1, 1, 2, 4] + ([0] * (n - 3))
    # If the value passed is in the cache (arr[n]), return it
    if n < 4:
        # Time complexity O(1)
        return arr[n]
    # For every cookie past our base case values
    # that value is the sum of the three before it
    # Assign that value to its proper index
    else:
        # Time complexity O(n)
        for i in range(4, n + 1):
            # Time complexity O(1)
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    # Return the value of the last index in the arr
    # Time complexity O(1)
    return arr.pop()

    # Overall: Time - O(n), Space - O(n)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
