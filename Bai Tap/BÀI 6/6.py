print('HO Duc Toan')
class Chuoi:
    def __init__(self):
        self.chuoi = ""

    def get_String(self):
        self.chuoi = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.chuoi.upper())


doi_tuong = Chuoi()
doi_tuong.get_String()
doi_tuong.print_String()
