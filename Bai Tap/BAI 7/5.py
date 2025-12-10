def file_read(fname):
    from itertools import islice
 
    with open(fname, "w", encoding='utf-8') as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")


    with open(fname, "r", encoding='utf-8') as txt:
        print(txt.read())

file_read('a.txt')
