a = input("Nhập list: ").split()
x = input("Nhập phần tử cần bỏ: ")
if x in a:
    a.remove(x)
print("List sau khi bỏ phần tử:", a)
