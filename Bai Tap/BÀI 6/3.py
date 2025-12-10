class Nguoi:
    def gioiTinh(self):
        return "Không xác định"


class Nam(Nguoi):
    def gioiTinh(self):
        return "Nam"


class Nu(Nguoi):
    def gioiTinh(self):
        return "Nữ"


a = Nam()
b = Nu()

print(a.gioiTinh())   
print(b.gioiTinh())  
