from tkinter import *
root = Tk()
root.geometry("700x500")
root.title("First GUI App")

# Important lable option
# text              -> adds the text on display
# bd or background  -> for set the background of application
# fg                -> foreground
# font              -> sets the font
#     1. font =("comicsansms", 20,"bold")
#     2. font ="comicsansmsn 20 bold"
# padx              -> padding in x
# pady              -> padding in y
# relief            -> how border show [SUNKEN,RAISED,GROOVE,RIDGE]

guru = Label(text="I am Rahul Gaur Coder of this GUI", bg="black", fg="white",padx ="40",
             pady="40", font =("comicsansms", 20,"bold"), borderwidth = 10, relief ="sunken")

# Important Pack Options
# anchor -> Give the  position for lable (nw, ne, .....)
# side  = top, bottom, left , right
# fill = always fill in x or y




guru.pack(side ="bottom", fill="x")
root.mainloop()
