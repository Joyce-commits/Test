# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Number Pad')
root.geometry('300x300')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

nums = [[1,2,3], [4,5,6], [7,8,9], ['#', 0, '*']]

for i in range(4):
	# Configure rows and columns to resize window
	root.columnconfigure(i, weight=1, minsize=100)
	root.rowconfigure(i, weight=1, minsize=75)
	for j in range(0, 3):
		frame = Frame(master=root,relief=RAISED, borderwidth=1)
		frame.grid(row=i, column=j)
		label = Label(master=frame, text=nums[i][j], bg="#ECFF18")
		label.pack(padx=3, pady=3)

# Start the GUI event loop
root.mainloop()