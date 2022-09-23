from typing import List
import time

class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        squares = [0 for _ in nums]

        high_index = len(nums) - 1
        left, right = 0, high_index

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                squares[high_index] = nums[right] * nums[right]
                right -= 1
            else:
                squares[high_index] = nums[left] * nums[left]
                left += 1

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
