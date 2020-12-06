CHARS = ord('z') - ord('a')

class Password():
    def __init__(self, password):
        print(f"Creating password {password}")
        self.password = password

    def next(self):
        return Password(num2string(string2num(self.password) + 1))

    def requirement1(self):
        p = self.password
        if not any(ord(p[i]) + 2 == ord(p[i + 2]) and
                   ord(p[i + 1]) + 1 == ord(p[i + 2])
                   for i in range(len(p) - 2)):
            return False

        return True

    def requirement2(self):
        if "i" in self.password or "o" in self.password or "l" in self.password:
            return False

        return True

    def requirement3(self):
        p = self.password
        skip = False
        found = []
        for i in range(len(p) - 1):
            if skip:
                skip = False
                continue
            if p[i] == p[i + 1] and p[i] not in found:
                skip = True
                found += [p[i]]

        return len(found) >= 2

    def is_valid(self):
        return self.requirement1 and self.requirement2 and self.requirement3


def num2string(num):
    num = int(num)
    vector = []
    while num > 0:
        vector = [num % CHARS] + vector
        num = int(num / CHARS)
    return "".join(reversed([nth_letter(v) for v in vector]))

def string2num(s):
    sum = 0
    for c in reversed(s):
        sum = sum * CHARS + ord(c) - ord('a')
    return sum


assert Password("hijklmmn").requirement1()
assert not Password("hijklmmn").requirement2()

assert Password("abbceffg").requirement3()
assert not Password("abbceffg").requirement1()

assert not Password("abbcegjk").requirement3()


def is_valid(password):
    """
    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    """
    return requirement1(password) and requirement2(password) and requirement3(password)

def increment(password):
    p = Password(password)
    while p.is_valid():
        p = p.next()
    return p.password

assert increment("abcdefgh") == "abcdffaa"
assert increment("ghijklmn") == "ghjaabcc"

def part1():
    pass
