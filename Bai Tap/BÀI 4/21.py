s = input("Nhập các số nhị phân 4 chữ số (cách nhau bởi dấu phẩy): ")
lst = s.split(',')
kq = [x for x in lst if int(x, 2) % 5 == 0]
print("Các số chia hết cho 5 là:", ','.join(kq))
