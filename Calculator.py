from tkinter import *
root = Tk()
root.geometry("1000x500")  # Width X Height
root.minsize(350,400)      # width , Height
root.maxsize(350,400)

def add():
    pass
def sub():
    pass
def mul():
    pass 
def div():
    pass

Label(root, text =":: CALCULATOR ::",pady="15",padx="120").grid(row =0)

display = StringVar()
Entry(root,textvariable =display,).grid(row = 2)


frame = Frame(root, borderwidth="6", bg  ="grey" , relief=SUNKEN).grid(row = 4)

b1 = Button(frame,text="+", command=add).grid(row = 5,column=0)
b2 = Button(frame,text="-", command=sub).grid(row = 5,column=0,ipadx =12)
b3 = Button(frame,text="X",command=mul).grid(row = 5,column=0)
b4 = Button(frame,text="/",command=div).grid(row = 5,column=0)
root.mainloop()