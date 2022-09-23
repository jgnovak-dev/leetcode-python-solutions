from typing import List
import time

class Solution:
    """
    Solution:
    """

    def sorted_squares(self, nums: List[int]) -> List[int]:
        """
        Solution:

        Create an empty list the size of nums filled with zeros.

        For each pass look at the square of the number on the left (left pointer),
        and the squares of the number on the right (right pointer).

        Using a tracking variable named 'high_index' which is used to insert
        larger numbers at the end of the array. Each pass decrement this number
        to fill the next largest spot.

        If the computed number at the left pointer is larger than the computed
        number at the right pointer, place it at the position tracked by 'high_index'
        and move the left pointer one place to the right.

        Otherwise the computed number at the right pointer is larger, place it in
        the position tracked by 'high_index' and move the right pointer one place
        to the left.

        Important detail that we are inserting the largest computed number at each
        pass, which is either the left side or the right side.

        Time complexity: O(n), must look at each element in nums.
        Space complexity: O(n), must store a value for each element in nums.

        Success:

        Runtime: 467ms, faster than 30% of Python3 submissions
        Mememory Usage: 16.3 MB, less than 49.35% of Python3 submissions

        """

        # Initialize a list of the same length as nums filled with 0s
        squares = [0 for _ in nums]

        num_len = len(nums) - 1
        # highest index used in compute
        high_index = num_len
        # pointers tracking the left and right side
        left, right = 0, num_len

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                squares[high_index] = left_square
                # walk the left pointer forward to the right
                left += 1
            else:
                squares[high_index] = right_square
                # walk the right pointer back to the left
                right -= 1

            high_index -= 1


        return squares


if __name__ == '__main__':
    start = time.process_time()
    solution = Solution()
    # correct answer: [0, 1, 9, 16, 100]
    print(f"Squares of a sorted array: {solution.sorted_squares([-4, -1, 0, 3, 10])}")
    # correct answer: [4, 9, 9, 49, 121]
    print(f"Squares of a sorted array: {solution.sorted_squares([-7, -3, 2, 3, 11])}")
    end = time.process_time()
    print(end - start)
