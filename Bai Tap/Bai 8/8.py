import tkinter as tk
from tkinter import ttk, messagebox

def show_choice():
    messagebox.showinfo("Thông báo", f"Bạn đã chọn nút: {choice.get()}")

root = tk.Tk()
root.title("Thông tin & Lựa chọn")


frame_info = ttk.LabelFrame(root, text="Thông tin cá nhân")
frame_info.grid(row=0, column=0, padx=10, pady=10, sticky="w")

ttk.Label(frame_info, text="Họ và tên:").grid(row=0, column=0, sticky="w")
ttk.Label(frame_info, text="Nguyễn Văn A").grid(row=0, column=1, sticky="w")

ttk.Label(frame_info, text="Ngày sinh:").grid(row=1, column=0, sticky="w")
ttk.Label(frame_info, text="01/01/2005").grid(row=1, column=1, sticky="w")

ttk.Label(frame_info, text="MSSV:").grid(row=2, column=0, sticky="w")
ttk.Label(frame_info, text="12345678").grid(row=2, column=1, sticky="w")

ttk.Label(frame_info, text="Ngành học:").grid(row=3, column=0, sticky="w")
ttk.Label(frame_info, text="Công nghệ thông tin").grid(row=3, column=1, sticky="w")


frame_radio = ttk.LabelFrame(root, text="Lựa chọn")
frame_radio.grid(row=1, column=0, padx=10, pady=10, sticky="w")

choice = tk.IntVar()
choice.set(1)

tk.Radiobutton(frame_radio, text="First",  variable=choice, value=1).grid(row=0, column=0)
tk.Radiobutton(frame_radio, text="Second", variable=choice, value=2).grid(row=0, column=1)
tk.Radiobutton(frame_radio, text="Third",  variable=choice, value=3).grid(row=0, column=2)

tk.Button(frame_radio, text="Click Me", command=show_choice).grid(row=0, column=3, padx=10)

root.mainloop()
