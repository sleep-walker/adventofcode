from collections import defaultdict


with open("05-input") as f:
    str_lines = f.read().splitlines()


def row(ticket):
    return int(ticket[:7].replace("F", "0").replace("B", "1"), base=2)


def seat(ticket):
    return int(ticket[7:].replace("L", "0").replace("R", "1"), base=2)


def seat_id(ticket):
    return row(ticket) * 8 + seat(ticket)


assert row("FBFBBFFRLR") == 44
assert seat("FBFBBFFRLR") == 5


def one(tickets):
    return max([seat_id(t) for t in tickets])


def two(tickets):
    seats = defaultdict(lambda: [None, None, None, None, None, None, None, None])
    for t in tickets:
        r = row(t)
        s = seat(t)
        print(f"row: {r} seat: {s}")
        seats[r][s] = True

    my_row = next(iter(x for x in seats if seats[x].count(None) == 1))
    my_seat = seats[my_row].index(None)

    return my_row * 8 + my_seat
