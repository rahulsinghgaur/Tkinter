from tkinter import *
from PIL import Image, ImageTk #If we want to take jpg image

root = Tk()
root.geometry("700x500")
# For Png Images
# photo = PhotoImage(file="img/logo.png")

# For Jpg Images
image = Image.open("img/img2.jpg")
photo = ImageTk.PhotoImage(image)

my_img = Label(image=photo)
my_img.pack()
root.mainloop()
