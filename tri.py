from tkinter import *

window = Tk()

window.title("Welcome to Table ")
photo = PhotoImage(file="tril.jpg")
lbl1 = Label(image=photo).grid(row=0,column=0,rowspan =100)
#lbl1.pack()
for i in range(1, 11):
    for j in range(1, 11):
        lbl = Label(window, text=(i * j), font=("Arial Bold", 20))
        lbl.grid(row=i,column=j,padx=2)
    lbl.grid(row=i,column=j)


window.mainloop()