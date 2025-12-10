print("HO DUC Toan")
print("245752021610162")

import modulecau5bai5
n = int(input("Nhập số lượng phần tử: "))

ds = []
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(value)

ds_sap_xep = modulecau5bai5.sap_xep(ds)
max_value = modulecau5bai5.tim_max(ds)
min_value = modulecau5bai5.tim_min(ds)

print("Danh sách sau khi sắp xếp:", ds_sap_xep)
print("Phần tử lớn nhất là:", max_value)
print("Phần tử nhỏ nhất là:", min_value)
