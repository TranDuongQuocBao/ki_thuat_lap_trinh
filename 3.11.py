import math

def Tinh():
    """
    Hàm tính chu vi và diện tích hình tròn.
    Yêu cầu nhập bán kính R từ bàn phím và kiểm tra tính hợp lệ (R >= 0).
    """
    print("--- CHƯƠNG TRÌNH TÍNH CHU VI VÀ DIỆN TÍCH HÌNH TRÒN ---")
    
    while True:
        try:
            R_input = input("Vui lòng nhập bán kính R của hình tròn: ")
            R = float(R_input)
            if R < 0:
                print("LỖI: Bán kính R phải là số không âm. Vui lòng nhập lại.")
            else:
                break 
        except ValueError:
            print("LỖI: Đầu vào không hợp lệ. Vui lòng nhập một giá trị số.")
    C = 2 * math.pi * R
    S = math.pi * (R ** 2)
    print(f"\n--- KẾT QUẢ TÍNH TOÁN (R = {R}) ---")
    print(f"1. Chu vi hình tròn (C) = 2 * π * R = {C:.4f}")
    print(f"2. Diện tích hình tròn (S) = π * R² = {S:.4f}")
    print("------------------------------------------")
    return C, S
Tinh()
