from tkinter import *
root = Tk()
root.geometry("700x500")

f1 = Frame(root, bg="grey", borderwidth = 6, relief =SUNKEN)
f1.pack(side = LEFT , fill=Y)

f2 = Frame(root, bg="grey", borderwidth = 8, relief =SUNKEN)
f2.pack(side = TOP , fill=X)

lb = Label(f1,text="Project Tkinter - PyCharm")
lb.pack(pady = 142)

lb = Label(f2,text="Welcome in sublime text editor",font="Helvetica 16 bold", fg="red", pady="10")
lb.pack()
root.mainloop()