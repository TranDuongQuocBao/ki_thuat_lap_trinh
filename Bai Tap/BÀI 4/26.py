t = 0
while True:
    s = input("Nhập giao dịch (D nạp, W rút, Enter để kết thúc): ")
    if not s:
        break
    type_trans, h = s.split()
    h = int(h)
    if type_trans == "D":
        t += h
    elif type_trans == "W":
        t -= h

print("Số dư hiện tại là:", t)
