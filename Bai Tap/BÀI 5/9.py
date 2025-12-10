def binary_search(lst, value):
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            lower = mid + 1
        else:
            upper = mid - 1

    return False


n = int(input("Nhập số phần tử n: "))
lst = []

print("Nhập các phần tử (tự động sắp xếp tăng dần):")
for i in range(n):
    x = int(input(f"Phần tử {i+1}: "))
    lst.append(x)

lst.sort()  
print("List sau sắp xếp:", lst)

value = int(input("Nhập phần tử cần tìm: "))

if binary_search(lst, value):
    print("True")
else:
    print("False")
