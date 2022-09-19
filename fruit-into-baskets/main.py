"""
Problem:

You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array 'fruits' where fruits[i] is the type of
fruit the 'ith' tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules
that you must follow:

    - You only have *two* baskets, and each basket can only hold a *single type* of fruit.
      There is no limit on the amount of fruit each baskent can hold.

    - Starting from any tree of your choice, you must pick *exactly one fruit* from *every*
      tree (including the start tree) while moving to the right. The picked fruits must fit
      in one of your baskets.

    - Once you reach a tree with fruit that cannot fit into your baskets, you must stop.

Given the integer array 'fruits', return the *maximum* number of fruits you can pick.

Example 1:

Input: fruits = [1, 2, 1]
Output: 3
Explanation: A fruit can be picked form each tree, two from tree '1' and one from tree '2'

Example 2:

Input: fruits = [0, 1, 2, 2]
Output: 3
Explanation: We can pick from trees [1, 2, 2].
If we had started from the first tree, we would only pick from trees [0, 1].

Example 3:

Input: fruits = [1, 2, 3, 2, 2]
Output: 4
Explanation: We can pick from trees [2, 3, 2, 2].
If we had started from the first tree, we would only pick from trees [2, 3, 2, 2].
"""

"""
Outcome:

Runtime: 2546ms, faster than 7.4% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 19.8MB, less than 89.1% of Python3 online submissions for Fruit Into Baskets.
"""


class Solution:
    def total_fruit(fruits) -> int:
        # The maximum baskets we can use
        MAX_BASKETS = 2

        # Initialize a pointer to the start of the window and the max_length
        window_left, max_length = 0, 0

        # Dictionary to track the fruits
        fruit_frequency = {}

        for window_right in range(len(fruits)):
            # The right most fruit is the one at this index in fruits
            right_fruit = fruits[window_right]

            # Check if the fruit is already in the dictionary
            if right_fruit not in fruit_frequency:
                # Add the fruit to the dictionary and initialize to zero so it can be incremented
                fruit_frequency[right_fruit] = 0

            # Increment the count for this fruit
            fruit_frequency[right_fruit] += 1


            # While the length of the fruit_frequency dictionary is greater than MAX_BASKETS
            while len(fruit_frequency) > MAX_BASKETS:
                # Get the left most fruit from the dictionary
                left_fruit = fruits[window_left]

                # Decrement the count of this fruit
                fruit_frequency[left_fruit] -= 1

                # If the count is now zero remove it from the dictionary
                if fruit_frequency[left_fruit] == 0:
                    del fruit_frequency[left_fruit]

                # Walk the left side of the window forward by 1, "shrinking" it
                window_left += 1

            # Compare max_length to the window size to see which is larger
            max_length = max(max_length, window_right - window_left + 1)

        # Return the max_length
        return max_length



if __name__ == '__main__':
    print(Solution.total_fruit([1, 2, 1]))
    print(Solution.total_fruit([0, 1, 2, 2]))
    print(Solution.total_fruit([1, 2, 3, 2, 2]))


