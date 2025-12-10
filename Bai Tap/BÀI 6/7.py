import math 
print('HỒ Duc Toan')
class Circle:
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh 
    def tinh_dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)
    def tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh 
hinhtron = Circle(5) 
print("Diện tích:", hinhtron.tinh_dien_tich())
print("Chu vi:", hinhtron.tinh_chu_vi())
