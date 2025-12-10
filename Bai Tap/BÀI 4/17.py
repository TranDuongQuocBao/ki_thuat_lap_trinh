n = int(input("Nhập số n: "))
for i in range(1, n):
    s = sum(j for j in range(1, i) if i % j == 0)
    if s > i:
        print(i)
