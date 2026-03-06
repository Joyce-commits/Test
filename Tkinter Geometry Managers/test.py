# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Number Pad')
root.geometry('300x300')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

nums = [[1,2,3], [4,5,6], [7,8,9], ['#', 0, '*']]


root.mainloop()