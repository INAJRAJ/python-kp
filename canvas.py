from tkinter import *
from tkinter.font import *



master=Tk()
canvas=Canvas(master)
canvas.pack()
canvas.create_text((20,20),text="Hello World!",fill="red", font="Helvetica 16 bold italic", anchor="nw")
canvas.create_text((20,40),text="Just do something!",fill="black", font="Helvetica 12 bold", anchor="nw")

master.mainloop()