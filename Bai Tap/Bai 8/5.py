import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x300")


v = tk.IntVar()
v.set(1)  

languages = [
    ("Python", 1),
    ("Pearl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print("Bạn đã chọn:", v.get())

tk.Label(root,
         text="Choose your favourite programming language:",
         justify=tk.LEFT,
         padx=20).pack()

for language, val in languages:
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("Custom Indicator Radio Buttons")
root.geometry("300x300")

v = tk.IntVar()
v.set(1)

languages = [
    ("Python", 1),
    ("Pearl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print("Bạn đã chọn:", v.get())

tk.Label(root,
         text="Choose your favourite programming language:",
         justify=tk.LEFT,
         padx=20).pack()


for language, val in languages:
    tk.Radiobutton(root,
                   text=language,
                   indicatoron=0,   
                   width=20,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()

