import math

def Tinh(R):
    if R <= 0:
        print("Bán kính không hợp lệ! (phải lớn hơn 0)")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    print("Chu vi hình tròn là:", chu_vi)
    print("Diện tích hình tròn là:", dien_tich)
R = float(input("Nhập bán kính hình tròn: "))
Tinh(R)
