def parse(row, header=False):
    return [
        cell.split("[s]-")[0 if header else 1]
        for cell 
        in row.strip()[1:-1].split(";")
        if "[s]-" in cell
    ]

# get keys
assert(parse("(a[s]-1;b[s]-hello;c[s]-has space)", True) == [
    "a",
    "b",
    "c"
])

# get value
assert(parse("(a[s]-1;b[s]-hello;c[s]-has space)") == [
    "1",
    "hello",
    "has space"
])

# parse list of FML lines
def translate(rows):
    header = parse(rows[0], True)
    return [header] + [parse(row) for row in rows]

# open basic.fml, translate it, and write to translated.csv
from csv import writer
with open("translated.csv", "w") as file:
    lines = open("basic.fml").readlines()
    writer(file).writerows(translate(lines))

# check that it matches the file I wrote manually
assert(open("translated.csv").read().strip() == open("basic.csv").read().strip())