a, b = 1, 2
total = 0

while a < 4000000:
    print(a, end=" ")
    if a % 2 == 0:
        total += a
    a, b = b, a + b

print()
print("numbers < 4000000:", total)
