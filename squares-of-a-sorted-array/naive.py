from typing import List
import time

class Solution:

    def sorted_squares(self, nums: List[int]) -> List[int]:
        for index, _ in enumerate(nums):
            value = nums[index]
            nums[index] = value * value

        return sorted(nums)


if __name__ == '__main__':
    start = time.process_time()
    solution = Solution()
    # correct answer: [0, 1, 9, 16, 100]
    print(f"Squares of a sorted array: {solution.sorted_squares([-4, -1, 0, 3, 10])}")
    # correct answer: [4, 9, 9, 49, 121]
    print(f"Squares of a sorted array: {solution.sorted_squares([-7, -3, 2, 3, 11])}")
    end = time.process_time()
    print(end - start)
