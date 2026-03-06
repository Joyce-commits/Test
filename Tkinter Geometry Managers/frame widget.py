from tkinter import *

window = Tk()
window.title("Sample Frame")
window.geometry("300x200")

# Frame 1
f1 = Frame(master=window)
f1.pack()

# Assigning a widget in frame 1
btn = Button(master=f1, text="click here", fg="red")
btn.pack()

# Frame 2
f2 = Frame(master=window, bg="yellow", height=100, width=200)
f2.pack()

window.mainloop()


