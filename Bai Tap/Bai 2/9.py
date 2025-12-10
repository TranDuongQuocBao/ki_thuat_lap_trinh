s = input("Enter a String: ")

d = {}
for i in s:
    d[i] = s.count(i)

print(d)
