
with open("04-input") as f:
    str_lines = f.read().splitlines()

required_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


class InvalidPassport(ValueError):
    def __init__(self, s):
        return super().__init__(f"Passport invalid: {s}")


class Passport():
    content = None
    required_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    def __getitem__(self, name):
        return self.content[name]

    def __setitem__(self, name, value):
        self.content[name] = value

    def keys(self):
        return self.content.keys()

    def __init__(self, s, validate_values=False):
        self.content = {}
        for token in [x for x in s.split(" ") if x != '']:
            k, _, v = token.partition(":")
            self[k] = v

        self.validate_keys()
        if validate_values:
            self.validate_values()

    def validate_keys(self):
        missing = self.required_keys.difference(self.keys())
        if missing:
            raise InvalidPassport(f"missing keys: {', '.join(missing)}")

    def validate_values(self):
        for field in self.required_keys:
            getattr(self, f"validate_{field}")()

    def _validate_range(self, field, value, min_value, max_value, length=None):
        self.validate_length(field, value, length)
        self.validate_number(field, value)
        if not (min_value <= int(value) <= max_value):
            raise InvalidPassport(f"{field} out of range: {min_value} <= {value} <= {max_value}")

    def validate_range_field(self, field, min_value, max_value, length=None):
        return self._validate_range(field, self[field], min_value, max_value, length)

    def validate_length(self, field, value, length):
        if length is not None and len(value) != length:
            raise InvalidPassport(f"field '{field}' has incorrect length ({length}): {value}")

    def validate_number(self, field, value):
        if not value.isdigit():
            raise InvalidPassport(f"field '{field}' is not a number: {value}")

    def validate_byr(self):
        return self.validate_range_field("byr", 1920, 2002, length=4)

    def validate_iyr(self):
        return self.validate_range_field("iyr", 2010, 2020, length=4)

    def validate_eyr(self):
        return self.validate_range_field("eyr", 2020, 2030, length=4)

    def validate_hgt(self):
        if self["hgt"].endswith("cm"):
            return self._validate_range("hgt", self["hgt"][:-2], 150, 193, length=3)
        elif self["hgt"].endswith("in"):
            return self._validate_range("hgt", self["hgt"][:-2],  59,  76, length=2)
        else:
            raise InvalidPassport(f"field 'hgt' doesn't have known unit")

    def validate_hcl(self):
        if not self["hcl"].startswith("#"):
            raise InvalidPassport(f"field 'hcl' doesn't start with '#': {self['hcl']}")
        self.validate_length("hcl", self["hcl"], 7)
        if not set(self["hcl"][1:]).issubset(set("0123456789abcdef")):
            raise InvalidPassport(f"field 'hcl' doesn't contain hex chars only: {self['hcl']}")

    def validate_ecl(self):
        if self["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            raise InvalidPassport(f"field 'ecl' not in set: {self['ecl']}")

    def validate_pid(self):
        self.validate_number("pid", self["pid"])
        self.validate_length("pid", self["pid"], 9)


def one_liners(lines):
    new = []
    buff = ""
    # force flush in the end
    if lines[-1] != "":
        lines.append("")

    for l in lines:
        if l == '':
            new.append(buff)
            buff = ""
        else:
            buff = buff + " " + l

    return new

lines = one_liners(str_lines)

def check(lines, validate_values):
    valid = invalid = 0
    for l in lines:
        try:
            Passport(l, validate_values=validate_values)
            valid += 1
        except InvalidPassport as e:
            print(e)
            invalid += 1
    print(f"valid: {valid}")
    print(f"invalid: {invalid}")
    return valid, invalid


def one(lines):
    return check(lines, False)

def two(lines):
    return check(lines, True)

test_lines = one_liners("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".splitlines())


assert one(test_lines) == (2, 2)

assert two(one_liners("""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
""".splitlines())) == (0, 4)

assert two(one_liners("""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""".splitlines())) == (4, 0)
