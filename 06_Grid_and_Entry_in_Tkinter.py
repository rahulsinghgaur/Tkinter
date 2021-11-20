from tkinter import *
root= Tk()
root.geometry("700x500")

def getValue():
    print(f"The user value is {uservalue.get()}")
    print(f"The Password is {passvalue.get()}")
    with open("value.txt", "a") as f:
        f.write(f"User name is : {uservalue.get()}\nPassword is : {passvalue.get()}\n")

user=Label(root, text="Username")
password = Label(root, text="Password")

user.grid()
password.grid()

# Variable class in tkinter(4 type)
# BooleanVar, DoubleVar,IntVar,StringVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row =1,column=1)

bt =Button(text="Submit", command=getValue)
bt.grid(row=2,column=0)
root.mainloop()
