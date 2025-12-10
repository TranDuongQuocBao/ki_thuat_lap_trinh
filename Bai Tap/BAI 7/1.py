
input_file = open('a.txt')

for line in input_file:
    line = line.rstrip('\n')  
    reversed_line = line[::-1]  
    print(reversed_line)

input_file.close()
