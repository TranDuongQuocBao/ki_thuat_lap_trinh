class ChuyenSoLaMa:
    def __init__(self):
        self.bang_gia_tri = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def la_ma_sang_so_nguyen(self, chuoi_la_ma):
        tong = 0
        gia_tri_truoc = 0
        for ky_tu in reversed(chuoi_la_ma.upper()):
            gia_tri = self.bang_gia_tri.get(ky_tu, 0)
            if gia_tri < gia_tri_truoc:
                tong -= gia_tri
            else:
                tong += gia_tri
            gia_tri_truoc = gia_tri
        return tong

bo_chuyen = ChuyenSoLaMa()
so_la_ma = "XIV"
so_nguyen = bo_chuyen.la_ma_sang_so_nguyen(so_la_ma)
print(f"Số La Mã {so_la_ma} = {so_nguyen}")
