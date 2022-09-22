"""
Problem description:

Given a characters array letters that is sorted in non-decreasing order and a character target,
return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"

Constraints:

- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter.
- letters is sorted in non-decreasing order.
- letters contains at least two different characters.
- target is a lowercase English letter.


Solution explanation:

This is ideal for a binary search: Let's find the rightmost position to insert target into
letters so that it remains sorted.

Our binary search (a typical one) proceeds in a number of rounds. At each round, let's maintain
the loop invariant that the answer must be in the interval [low, high]. Let mid = (low + high) / 2.
If letters[mid] <= target, then we must insert it in the interval [mi + 1, hi].

Otherwise, we must insert it in the interval [low, mi].

At the end, if our insertion position says to insert target into the last position letters.length,
we return letters[0] instead. This is what the modulo operation does.

Success:

Runtime: 271, faster than 9.49%
Memory Usage: 14.3MB, less than 60.1%

"""

from typing import List

def next_greatest_letter(letters: List[str], target: str) -> str:
    """
    Do the thing
    """
    low, high = 0, len(letters) - 1

    # Edge case where the target letter is at the end of the array
    # if letters[-1] == target or letters[-1] < target:
    #     return letters[0]
    if letters[-1] <= target:
        return letters[0]

    while low < high:
        mid = (low + high) // 2

        if letters[mid] <= target:
            # letter is smaller than or equal to the target
            low = mid + 1
        else:
            # letter is greater than the target
            high = mid

    return letters[low % len(letters)]


if __name__ == '__main__':
    print(next_greatest_letter(["c", "f", "j"], "a"))
    print(next_greatest_letter(["c", "f", "j"], "c"))
    print(next_greatest_letter(["c", "f", "j"], "d"))
    print(next_greatest_letter(["c", "f", "j"], "j"))
    print(next_greatest_letter(["c", "f", "j"], "k"))
