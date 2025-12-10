from tkinter import *

window = Tk()
window.title("Demo Tkinter")
window.geometry("350x200")


lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)


def clicked():
    lbl.configure(text="Button was clicked !!!")


btn = Button(window, 
             text="Click Me", 
             command=clicked,
             bg="lightblue",   
             fg="red")         

btn.grid(column=0, row=0)

window.mainloop()
