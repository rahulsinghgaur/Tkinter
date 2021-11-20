from tkinter import *
root=Tk()
root.geometry("700x500")


Label(root, text ="Welcome to Tkinter GUI Application",pady="15").grid(row =0,column=3)

Label(root , text = "Name").grid(row =1,column=2)
Label(root, text="Phone").grid(row =2,column=2)
Label(root, text ="Gender").grid(row =3,column=2)
Label(root, text ="Product").grid(row =4,column=2)
Label(root, text="Payment Mode").grid(row =5,column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
productvalue = StringVar()
paymentmodevalue = StringVar()
iagree = IntVar()

Entry(root, textvariable = namevalue).grid(row =1,column=3)
Entry(root, textvariable =phonevalue).grid(row =2,column=3)
Entry(root, textvariable= gendervalue).grid(row =3,column=3)
Entry(root, textvariable=productvalue).grid(row =4,column=3)
Entry(root, textvariable =paymentmodevalue).grid(row =5,column=3)
Checkbutton(text ="I am agree T&C", variable=iagree).grid(row =6,column=3)


def getValue():
    str =f"Name : {namevalue.get()}\nPhone : {phonevalue.get()}\nGender : " \
         f"{gendervalue.get()}\nProduct : {productvalue.get()}\nPayment Mode :" \
         f" {paymentmodevalue.get()}\nAgree : {iagree.get()}\n"
    print(str)
    with open("Form.txt", "a") as f:
        f.write(str)

Button(text ="Submit", command= getValue).grid(row=7,column=3)


root.mainloop()