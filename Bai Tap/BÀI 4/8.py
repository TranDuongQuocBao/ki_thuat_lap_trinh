s = input("Nhập dãy từ: ")

ds = s.split()                      
max_len = max(len(t) for t in ds)   


tu_dai_nhat = [t for t in ds if len(t) == max_len]

print("Độ dài lớn nhất:", max_len)
print("Các từ dài nhất:")
for t in tu_dai_nhat:
    print(t)
