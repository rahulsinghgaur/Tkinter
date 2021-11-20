from tkinter import *

root = Tk()
root.geometry("1000x500")  # Width X Height
root.minsize(300,200)      # width , Height
root.maxsize(1100,800)

lb = Label(text = "I am a Programmer")
lb.pack()
root.mainloop()

