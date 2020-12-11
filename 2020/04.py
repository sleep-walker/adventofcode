
with open("04-input") as f:
    str_lines = f.read().splitlines()

required_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def read_one(line):
    print(f"validating: '{line}'")
    result = {}
    # split by space
    tokens = line.split(" ")
    # filter empty parts
    tokens = [x for x in tokens if x != '']
    for token in tokens:
         k, _, v = token.partition(":")
         result[k] = v

    return result


def validate(passport, simple=True):
    keys = set(passport.keys())
    if not required_keys.issubset(keys):
        missing = required_keys.difference(keys)
        print(f" invalid: missing: {missing}")
        return False

    if simple:
        return True

    if not (passport["byr"].isdigit() and 1920 <= int(passport["byr"]) <= 2020):
        print(f" invalid: byr out of range")
        return False

    if not (passport["iyr"].isdigit() and 2010 <= int(passport["iyr"]) <= 2020):
        print(f" invalid: iyr out of range")
        return False

    if not (passport["eyr"].isdigit() and 2020 <= int(passport["eyr"]) <= 2030):
        print(f" invalid: eyr out of range")
        return False

    if passport["hgt"].endswith("cm"):
        cm = passport["hgt"][:-(len("cm"))]
        if not cm.isdigit():
            print(f" invalid: hgt not a number: {cm}")
            return False
        if not (150 <= int(cm) <= 193):
            print(f" invalid: hgt not in range: {passport['hgt']}")
            return False
    elif passport["hgt"].endswith("in"):
        inch = passport["hgt"][:-(len("in"))]
        if not inch.isdigit():
            print(f" invalid: hgt not a number: {inch}")
            return False
        if not (59 <= int(inch) <= 76):
            print(f" invalid: hgt not in range: {passport['hgt']}")
            return False
    else:
        print(" invalid: hgt has no unit: {passport['hgt']}")
        return False

    if not (passport["hcl"].startswith("#") and len(passport["hcl"]) == 7 and all([c in "0123456789abcdef" for c in passport["hcl"][1:]])):
        print(" invalid: hcl: {passport['hcl']}")
        return False

    if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        print(f" invalid: ecl not in set: {passport['ecl']}")
        return False

    if not (passport["pid"].isdigit() and len(passport["pid"]) == 9):
        print(f" invalid: pid of len {len(passport['pid'])}: '{passport['pid']}'")
        return False

    return True



def read_all(lines, simple):
    valid = 0
    count = 0
    last = ""
    # force flush in the end
    if lines[-1] != "":
        lines.append("")

    for l in lines + [""]:
        if l == '':
            # flush
            if last == "":
                continue
            count += 1
            passport = read_one(last)
            if validate(passport, simple):
                valid += 1
            last = ''
        else:
            last = last + " " + l

    return count, valid

test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".splitlines()


assert read_all(test_input, True) == (4, 2)

assert read_all("""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""".splitlines(), False) == (4, 0)

assert read_all("""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""".splitlines(), False) == (4, 4)
