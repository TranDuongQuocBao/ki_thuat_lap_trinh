import math
x,y = 0,0
print("Nhập các lệnh di chuyển")
while True:
    s = input("> ")
    if not s:
        break
    try:
        movement = s.split()
        direction = movement[0].upper()
        steps = int(movement[1])
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
    except (IndexError, ValueError):
        print("Lỗi: Vui lòng nhập <HƯỚNG> <SỐ BƯỚC>.")
        print("Lỗi: Số bước di chuyển phải là số nguyên.")
        print(f"Có lỗi xảy ra: {e}")
distance = math.sqrt(x**2 + y**2)
print(f"\nVị trí cuối cùng: ({x}, {y})")
print(f"Khoảng cách (số nguyên gần nhất): {int(round(distance))}")
