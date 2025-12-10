a = input("Nhập list: ").split()
x = input("Nhập phần tử cần tìm: ")
if x in a:
    print(x, "có trong list.")
else:
    print(x, "không có trong list.")
