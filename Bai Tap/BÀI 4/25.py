nums = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
odd_nums = [n for n in nums if n % 2 != 0]
print("Các số lẻ là:", odd_nums)
