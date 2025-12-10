def file_read_from_tail(fname, nlines):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[-nlines:]:
            print(line.rstrip())

file_read_from_tail('a.txt', 2)
