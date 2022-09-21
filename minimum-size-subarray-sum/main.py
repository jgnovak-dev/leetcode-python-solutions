"""
Problem:

Given an array of positive integers 'nums' and a positive integer 'target', return the minimal length
of a contiguous subarray of which the sum is greater than or equal to 'target'. If there is no subarray
of contiguous (one or more) elements that are greater than or equal to the target return 0.

Example 1:

Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2
Explanation: The subarray [4, 3] has the minimal length under the problem constraint. In other words
it took two elements, 4 and 3 to equal the target.

Example 2:

Input: target = 4, nums = [1, 4, 4]
Output: 1
Explanation: The subarray [4] has the minimal length under the problem constraints. In other words
it took one element [4] to equal the target.

Example 3:

Input: target = 11, nums [1, 1, 1, 1, 1, 1, 1, 1]
Output: 0
Explanation: There are no elements in the array that added together are equal to or greater than
the target.

"""

"""
Solution:

Sliding Window pattern where we will walk the array of numbers to the right adding to a running
sum until the sum is greater than or equal to the target.

While the running sum is greater than or equal to the target we will subtract the left most value
from the array from the running sum and walk the left side of the window forward one place per pass.

This question is really asking how many elements in the array it takes to add up to the target.
We'll need to track this with a variable that will be initially set to 'infinity'.

If we reach the end and the tracking variable is still 'infinity' we know that we did not find any
elements that add up to or are greater than the target.

Otherwise, we can return the value of the tracking variable that is updated each time we shrink the
window.

"""

"""
Success:

Runtime: 526ms, faster than 30.5% of Python3 submissions.
Memory Usage: 27.2MB, less than 43.5% of Python3 submissions.
"""

import math

from typing import List

def min_subarray_len(target: int, nums: List[int]) -> int:
    # Initialize the window_sum and window_start to 0
    window_sum, window_start = 0, 0
    # Initialize min_length to infinity so we know if min_length was never updated
    min_length = math.inf

    # Loop over the array from 0 to the length of the array
    for window_end in range(0, len(nums)):
        # Add this element to the running sum
        window_sum += nums[window_end]

        # While the value of window_sum is greater than the value of target
        while window_sum >= target:
            # Determine which is smaller between min_length and the distance between
            # window_end and window_start + 1. Remember to account for zero based.
            min_length = min(min_length, window_end - window_start + 1)
            # Remove the leftmost value from the window_sum to "shrink" the window on the left
            window_sum -= nums[window_start]
            # Move the left side of the window forward by one place
            window_start += 1

    # If the minimum length is infinity return 0
    if min_length == math.inf:
        return 0

    # Return the minimum length
    return min_length


if __name__ == '__main__':
    numbers = [int(x) for x in input().strip()]
    target = int(input().strip())
    result = min_subarray_len(target, numbers)
    print(result)
