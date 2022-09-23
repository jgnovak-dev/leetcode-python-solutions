from typing import List
import time

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result

if __name__ == '__main__':
    start = time.process_time()
    solution = Solution()
    # correct answer: [0, 1, 9, 16, 100]
    print(f"Squares of a sorted array: {solution.sortedSquares([-4, -1, 0, 3, 10])}")
    # correct answer: [4, 9, 9, 49, 121]
    print(f"Squares of a sorted array: {solution.sortedSquares([-7, -3, 2, 3, 11])}")
    end = time.process_time()
    print(end - start)
