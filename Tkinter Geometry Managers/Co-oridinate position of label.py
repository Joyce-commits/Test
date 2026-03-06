from tkinter import *

window = Tk()

window.geometry("500x500")

label1 = Label(text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = Label(text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

label3 = Label(text="I'm at (100, 100)", bg="blue")
label3.place(x=100, y=100)

window.mainloop()