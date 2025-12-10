""" Chương trình tạo một máy tính đơn giản có thể cộng, trừ, nhân và
chia bằng cách sử dụng các hàm (functions). """
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Lỗi: Không thể chia cho 0"
    return x / y
print("--- CHỌN PHÉP TÍNH ---")
print("1. Cộng (Add)")
print("2.Trừ (Subtract)")
print("3. Nhân (Multiply)")
print("4.Chia (Divide)")
print("-----------------------")
while True:
    choice = input("Nhập lựa chọn (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
        except ValueError:
            print("Lỗi: Đầu vào không hợp lệ. Vui lòng chỉ nhập số.")
            continue
        ket_qua = None 
        if choice == '1':
            ket_qua = add(num1, num2)
            phep_tinh = '+'
        elif choice == '2':
            ket_qua = subtract(num1, num2)
            phep_tinh = '-'
        elif choice == '3':
            ket_qua = multiply(num1, num2)
            phep_tinh = '*'
        elif choice == '4':
            ket_qua = divide(num1, num2)
            phep_tinh = '/'
        if isinstance(ket_qua, str) and "Lỗi" in ket_qua:
            print(ket_qua)
        else:
            print(f"{num1} {phep_tinh} {num2} = {ket_qua}")
        tiep_tuc = input("Bạn có muốn thực hiện phép tính khác không? (có/không): ")
        if tiep_tuc.lower() != 'có':
            break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1, 2, 3, hoặc 4.")

print("\nCảm ơn đã sử dụng máy tính!")
