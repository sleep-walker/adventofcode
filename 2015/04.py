from hashlib import md5
import itertools

def hash_starts_with(key, start):
    bkey = key.encode("utf-8")
    for i in itertools.count(start=1):
        bi = str(i).encode("utf-8")
        if md5(bkey + bi).hexdigest().startswith(start):
            return i

def part_1(key):
    return hash_starts_with(key, "00000")

def part_2(key):
    return hash_starts_with(key, "000000")

assert part_1("abcdef") == 609043
assert part_1("pqrstuv") == 1048970

