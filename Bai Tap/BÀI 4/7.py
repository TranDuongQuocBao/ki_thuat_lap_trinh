s = input("Nhập chuỗi: ")

ket_qua = ""
for ch in s:
    if not ch.isdigit():   
        ket_qua += ch

print("Chuỗi sau khi loại bỏ chữ số:", ket_qua)
