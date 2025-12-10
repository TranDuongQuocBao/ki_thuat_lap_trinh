import os

duongdan = os.path.join(os.path.expanduser("~"), "Downloads")
tep1 = os.path.join(duongdan, "kythuatlaptrinh111.txt")
tep2 = os.path.join(duongdan, "kythuatlaptrinh222.txt")

with open(tep1, "r", encoding="utf-8") as t:
    noidung = t.read()

with open(tep2, "w", encoding="utf-8") as t:
    t.write(noidung)

print("Da sao chep xong tu tep 111 sang tep 222")
