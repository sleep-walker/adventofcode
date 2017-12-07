def is_valid(pwd):
    # split to words
    s = pwd.split(" ")
    # set removes duplicities...
    #  if length of set is same as of a list, there are no duplicities
    return len(set(s)) == len(s)

def is_valid2(pwd):
    # split to words
    s = pwd.split(" ")
    # sort letters in word
    s = ["".join(sorted(list(x))) for x in s]
    # check for duplicities again
    return len(set(s)) == len(s)

# read input file
with open("04-input") as f:
    l = f.read().splitlines()

# filter only valid passwords
valid = filter(is_valid, l)
valid2 = filter(is_valid2, l)
# print length
print len(valid), len(valid2)
