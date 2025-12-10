print("HO Duc Toan")
print("245752021610012")
import modulecau5bai5
n = int(input("Nhập số lượng phần tử trong danh sách: "))

lst = []
for i in range(n):
   x = float(input(f"Nhập phần tử thứ {i+1}: "))
   lst.append(x)

sapxep= modulecau5bai5.sap_xep(lst)
maxx = modulecau5bai5.tim_max(lst)
minn =sapxep[0]

print("Danh sách sau khi sắp xếp:", sapxep)
print("Phần tử nhỏ nhất:", minn)
print("Phần tử lớn nhất:", maxx)

vitri1= sapxep.index(maxx)
vitri2= sapxep.index(minn)
print("vi trí của giá trị lớn nhất là",vitri1+1)
print("vi trí của giá trị nhỏ nhất là",vitri2+1)
