from re import I
from typing import List

def next_greatest_letter(letters: List[str], target: str) -> str:
    low, high = 0, len(letters)

    while low < high:
        mid = (low + high) // 2

        if ord(letters[mid]) > ord(target):
            high = mid
        else:
            low = mid + 1

    return letters[low % len(letters)]


if __name__ == '__main__':
    print(next_greatest_letter(["c", "f", "j"], "a"))
    print(next_greatest_letter(["c", "f", "j"], "c"))
    print(next_greatest_letter(["c", "f", "j"], "d"))
    print(next_greatest_letter(["c", "f", "j"], "j"))
    print(next_greatest_letter(["c", "f", "j"], "k"))
