from tkinter import *


def clicked():
 
    lbll.configure(text="Button was clicked !!")

def clickd():
 
    res = "Welcome to " + txt.get()
 
    lbll.configure(text= res)
    
window = Tk()
window.geometry('350x200')
window.title("Welcome to LikeGeeks app")
lbll = Label(window, text="Hello")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
 
btn = Button(window, text="Click Me", command=clicked)
btnr = Button(window, text="Click Me", command=clickd, bg="orange", fg="red") 
btn.grid(column=3, row=0)
btnr.grid(column=4, row=0)
txt = Entry(window,width=10)
txt.grid(column=2, row=0)
lbll.grid(column=0, row=0)
lbl.grid(column=1, row=0)
window.mainloop()
