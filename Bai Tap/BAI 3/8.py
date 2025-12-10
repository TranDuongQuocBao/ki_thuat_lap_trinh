import math

pos = [0, 0]

while True:
    s = input("Nhập hướng và số bước (UP/DOWN/LEFT/RIGHT), hoặc Enter để dừng: ")
    if not s:
        break

    movement = s.split()
    direction = movement[0].upper()
    steps = int(movement[1])
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        print("Hướng không hợp lệ! Vui lòng nhập lại.")

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
