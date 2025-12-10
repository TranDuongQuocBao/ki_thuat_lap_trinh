n = int(input("Nhập số tự nhiên n (>0): "))

if n > 0:
    for i in range(n, -1, -1):
        print(i)
else:
    print("Vui lòng nhập số tự nhiên lớn hơn 0!")
