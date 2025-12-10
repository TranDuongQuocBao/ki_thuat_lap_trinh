passwords = input("Nhập các mật khẩu, cách nhau bằng dấu phẩy: ")
list_pw = passwords.split(",")
valid_pw = []

for pw in list_pw:
    if len(pw) < 6 or len(pw) > 12:
        continue

    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu = False

    for ch in pw:
        if ch >= 'a' and ch <= 'z':
            co_chu_thuong = True
        elif ch >= 'A' and ch <= 'Z':
            co_chu_hoa = True
        elif ch >= '0' and ch <= '9':
            co_so = True
        elif ch in "$#@":
            co_ky_tu = True

    if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu:
        valid_pw.append(pw)

print("Mật khẩu hợp lệ là:", ",".join(valid_pw))
