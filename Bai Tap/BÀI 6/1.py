print("Ho Duc Toan")
import math
class Circle:
    def __init__(self, ban_kinh):
        self.r = ban_kinh   
    
    def dien_tich(self):
        return math.pi * self.r ** 2

if __name__ == "__main__":
    r = float(input("Nhập bán kính hình tròn: "))
    hinh_tron = Circle(r)
    
    
    s = hinh_tron.dien_tich()
    print(f"Diện tích (làm tròn 2 chữ số): {s:.2f}")
