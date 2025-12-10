S = input("Nhập chuỗi S: ")
for ch in S:
    print(ch)

S = input("Nhập chuỗi S: ")
for ch in S:
    if not ch.isspace():
       print(ch)

S = input("Nhập chuỗi S: ")
for ch in S:
    print(ch.upper())

lst = input("Nhập danh sách: ").split()
print("Danh sách vừa nhập là:", lst)

words = input("Nhập danh sách các từ: ").split()
print("Danh sách vừa nhập là:", words)
print("Danh sách theo thứ tự ngược lại là:", words[::-1])
