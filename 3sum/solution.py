# Problem statement:
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#
#
# Example 2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
# Constraints:
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
#
# Time complexity: O(n^2)
# Space complexity: O(n), a data structure is created to store output
#


from typing import List


class Solution:
    """
    Do the thing
    """
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Do the thing
        """
        result = []
        nums.sort()

        for i, _ in enumerate(nums):
            # if the current value is greater than 0
            if nums[i] > 0:
                # break to skip it
                break
            # if the current value is the same as the one before, skip it
            if i == 0 or nums[i - 1] != nums[i]:
                self.two_sum_it(nums, i, result)

        return result

    def two_sum_it(self, nums: List[int], i: int, result: List[List[int]]):
        """
        Do the thing
        """
        low, high = i + 1, len(nums) - 1

        while low < high:
            the_sum = nums[i] + nums[low] + nums[high]

            if the_sum < 0:
                low += 1
            elif the_sum > 0:
                high -= 1
            else:
                # triplet found
                result.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1

                # increment low while the next value is the same as the previous one
                # to avoid duplicates
                while low < high and nums[low] == nums[low - 1]:
                    low += 1


if __name__ == '__main__':
    solution = Solution()
    # correct answer: [[-1, -1, 2], [-1, 0, 1]]
    print(f"3sum: {solution.three_sum([-1, 0, 1, 2, -1, -4])}")
    # correct answer: []
    print(f"3sum: {solution.three_sum([0, 1, 1])}")
    # correct answer: [[0, 0, 0]]
    print(f"3sum: {solution.three_sum([0, 0, 0])}")
