def next_greatest_letter(letters, target):
    for c in letters:
        if c > target:
            return c

    return letters[0]


if __name__ == '__main__':
    print(next_greatest_letter(["c", "f", "j"], "a"))
    print(next_greatest_letter(["c", "f", "j"], "c"))
    print(next_greatest_letter(["c", "f", "j"], "d"))
