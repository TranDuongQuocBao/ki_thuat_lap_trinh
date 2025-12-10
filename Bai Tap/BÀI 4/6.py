ho_name = input("Nhập họ và tên: ").strip()
parts = ho_name.split()
if len(parts) == 2:
    ho = parts[0]
    ten = parts[1]
    print("Họ là:", ho)
    print("Tên riêng là:", ten)
else:
    print("Vui lòng nhập đúng định dạng: chỉ gồm họ và tên riêng (2 từ).")
