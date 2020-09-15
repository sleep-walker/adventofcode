with open("05-input") as f:
    contents = f.read().splitlines()

def is_nice1(word):
    three_vowels = 3 <= sum((1 for c in word if c in ('a', 'e', 'i', 'o', 'u')))
    repeating_char = any((1 for i, j in zip(word, word[1:]) if i == j))
    no_forbidden = not any((1 for forbidden in ("ab", "cd", "pq", "xy") if forbidden in word))

    return three_vowels and repeating_char and no_forbidden

assert is_nice1("ugknbfddgicrmopn")
assert is_nice1("aaa")

assert not is_nice1("jchzalrnumimnmhp")
assert not is_nice1("haegwjzuvuyypxyu")
assert not is_nice1("dvszwmarrgswjxmb")

def part_1(contents):
    return sum((1 for word in contents if is_nice1(word)))


def is_nice2(word):
    repeating_two_chars = False
    for i in range(len(word) - 1):
        if word[i] + word[i + 1] in word[i+2:]:
            repeating_two_chars = True
            break
    repeating_char_with_middle = any((1 for i, j in zip(word, word[2:]) if i == j))
    return repeating_char_with_middle and repeating_two_chars

assert is_nice2("qjhvhtzxzqqjkmpb")
assert is_nice2("xxyxx")
assert not is_nice2("uurcxstgmygtbstg")
assert not is_nice2("ieodomkazucvgmuy")

def part_2(contents):
    return sum((1 for word in contents if is_nice2(word)))
