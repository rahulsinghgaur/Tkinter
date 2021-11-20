from tkinter import *
root = Tk()
root.geometry("700x500")
root.title("Button in kinter")

def login():
    print("Login Successful")
def signUp():
    print("Sign Up Successful")
def submit():
    print("Submit Successful")
def cancel():
    print("Cancel Successful")
frame = Frame(root, borderwidth="6", bg  ="grey" , relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame,text="Login", command=login)
b1.pack(side =LEFT)
b2 = Button(frame,text="SignUp", command=signUp)
b2.pack(side =LEFT)
b3 = Button(frame,text="Submit",command=submit)
b3.pack(side =LEFT)
b4 = Button(frame,text="Cancel",command=cancel)
b4.pack(side =LEFT)



root.mainloop()