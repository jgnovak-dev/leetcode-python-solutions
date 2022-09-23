# Problem statement:
#
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
# that each unique element appears only once. The relative order of the elements should be kept
# the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have
# the result be placed in the first part of the array nums. More formally, if there are k elements
# after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array
# in-place with O(1)
# extra memory.
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2
# respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1,
# 2, 3, and 4  respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
#
# Time complexity: O(n), must look at every element
# Space complexity: O(1), no additional data structure was used
#


from typing import List

class Solution:
    """
    Doing the thing
    """
    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Doing the thing
        """
        # starting from the second index (1)
        next_non_duplicate = 1

        for i, _ in enumerate(nums):
            # if the previous number is not equal to this number
            if nums[next_non_duplicate - 1] != nums[i]:
                # insert this number in nums at index i
                nums[next_non_duplicate] = nums[i]
                # advance the pointer
                next_non_duplicate += 1

        return next_non_duplicate


if __name__ == '__main__':
    solution = Solution()
    # correct answer: 2
    print(f"Duplicates removed: {solution.remove_duplicates([1, 1, 2])}")
    # correct answer 5
    print(f"Duplicates removed: {solution.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])}")
