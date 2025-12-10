n = int(input("Nhập số nguyên n: "))
a, b = 0, 1
fib = []
while a < n:
    fib.append(a)
    a, b = b, a + b
print("Các số Fibonacci nhỏ hơn", n, "là:", fib)
