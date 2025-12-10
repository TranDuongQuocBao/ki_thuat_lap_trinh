def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname, 'r', encoding='utf-8') as f:
        for line in islice(f, nlines):
            print(line.rstrip())

file_read_from_head('a.txt', 2)
