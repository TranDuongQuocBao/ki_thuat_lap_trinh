print("HỒ Đức Toàn")
class Hinhchunhat:
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def dientich(self):
        return self.chieudai * self.chieurong


dai= float(input('nhap chieu dai hinh chư nhật: '))
rong= float(input('nhap chieu rong hinh chư nhật: '))
hcn = Hinhchunhat(dai,rong)
print("Diện tích hình chữ nhật là:", hcn.dientich())
