print('HO Duc Toan')
class DaoNguocChuoi:
    def __init__(self, chuoi):
        self.chuoi = chuoi

    def dao_nguoc_tung_tu(self):
        danh_sach_tu = self.chuoi.split()
        danh_sach_tu_dao_nguoc = [tu[::-1] for tu in danh_sach_tu]
        chuoi_moi = ' '.join(danh_sach_tu_dao_nguoc)
        return chuoi_moi

chuoi_goc = "Hello world from Python"
doi_tuong = DaoNguocChuoi(chuoi_goc)
chuoi_dao_nguoc = doi_tuong.dao_nguoc_tung_tu()
print("Chuỗi gốc:", chuoi_goc)
print("Chuỗi sau khi đảo ngược từng từ:", chuoi_dao_nguoc)
