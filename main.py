def parse(row):
    from re import search
    types = { "s": str, "i": int, "f": float }
    cells = [
        search(r"^(.+)\[([\w])\]-(.+)", cell).groups()
        for cell 
        in row.strip()[1:-1].split(";")
    ]
    return { cell[0]: types[cell[1]](cell[2]) for cell in cells }

# parse list of FML lines
def translate(rows, header):
    return [
        [
            row[col] if col in row else "NAN"
            for col in header
        ]
        for row in [parse(row) for row in rows]
    ]

def main():
    from csv import writer
    from sys import stdin, stdout, argv
    lines = stdin.readlines()
    header = argv[1:]
    writer(stdout).writerow(header)
    writer(stdout).writerows(translate(lines, header))

if __name__ == "__main__": main()
