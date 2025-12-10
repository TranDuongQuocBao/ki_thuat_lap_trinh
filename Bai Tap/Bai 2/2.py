import math

def khoang_cach(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(khoang_cach(5, 2, 4, 5))
