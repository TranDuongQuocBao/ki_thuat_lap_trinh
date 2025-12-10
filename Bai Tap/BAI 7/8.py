def write_list_to_file(filename, data_list):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data_list:
            f.write(str(item) + "\n")

my_list = ["Python", "Java", "C++", 123, True]
write_list_to_file("a.txt", my_list)
