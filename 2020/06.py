
with open("06-input") as f:
    str_lines = f.read().splitlines()


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
            if buff:
                buff = buff + " " + l
            else:
                buff = l

    return new

lines = one_liners(str_lines)

def handle_group(line):
    people = line.split(" ")
    answers = "".join(people)
    num_people = len(people)
    num_questions = len(set(answers))
    num_all_questions = len([c for c in set(answers) if answers.count(c) == num_people])
    return num_people, num_questions, num_all_questions

def one(lines):
    count = 0
    for l in lines:
        p, c, a = handle_group(l)
        count += c
    return count

def two(lines):
    count = 0
    for l in lines:
        p, c, a = handle_group(l)
        print(f"{p}, {c}, {a}")
        count += a
    return count

