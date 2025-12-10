ds = input('Nhap chuoi: ').split()

x = ds[0:-1]
for c in x:
    print(c)
ds.remove('123')
for ch in ds:
    print(ch)
print("vị trí của chuỗi abc là", ds.index('abc'))
ds.sort()
for ch in ds:
    print(ch)