def parse(row):
    from re import split, search
    types = { "s": str, "i": int, "f": float }
    cells = [ 
        search(r"^(.+)\[([\w])\]-(.+)", cell).groups()
        for cell 
        in row.strip()[1:-1].split(";")
    ]
    return { cell[0]: types[cell[1]](cell[2]) for cell in cells }

assert(parse("(a[i]-1;b[s]-hello;c[f]-1.5)") == {
    "a": 1,
    "b": "hello",
    "c": 1.5,
})

# parse list of FML lines
def translate(rows, header):
    rows = [parse(row) for row in rows]
    return [header] + [
        [row[col] or "NAN" for col in header]
        for row
        in rows
    ]

# open basic.fml, translate it, and write to translated.csv
def main():
    from csv import writer
    from sys import stdin, stdout, argv
    lines = stdin.readlines()
    writer(stdout).writerows(translate(lines, argv[1:]))

if __name__ == "__main__": main()
