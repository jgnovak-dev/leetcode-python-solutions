"""
Problem:

Given two strings 's1' and 's2', return 'true' if 's2' contains a permutation of 's1' or 'false' otherwise.

In other words, return 'true' if one of 's1s' permutations is in the substring 's2'.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 < s1.length, s2.length <= 10(4)
s1 and s2 consist of lowercase English letters.

Success:

Runtime: 141ms, faster than 53.3% of Python3 online submissions for Permutation in a string.
Memory Usage: 13.9 MB less than 95.45% of Python3 online submissions for Permutation in a string.

"""
def check_inclusion(self, permutation: str, astring: str) -> bool:
    window_start, matched = 0, 0
    char_frequency = {}

    for char in permutation:
        if char not in char_frequency:
            char_frequency[char] = 0

        char_frequency[char] += 1

    for window_end in range(len(astring)):
        right_char = astring[window_end]

        if right_char in char_frequency:
            # decrement the frequency of matched characters
            char_frequency[right_char] -= 1

            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # Shrink the window by one character
        if window_end >= len(permutation) - 1:
            left_char = astring[window_start]

            window_start += 1

            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1

                char_frequency[left_char] += 1

    return False


if __name__ == '__main__':
    first_string = input("Permutation string: ").strip()
    second_string = input("Main string: ").strip()
    print(check_inclusion(first_string, second_string))


