
k = open('a.txt', 'r')

char = 0  
wc = 0     
lc = 0     

for line in k:
    lc += 1
    char += len(line)

    words = line.split()
    wc += len(words)

k.close()

print("The no. of chars is %d" % char)
print("The no. of words is %d" % wc)
print("The no. of lines is %d" % lc)
