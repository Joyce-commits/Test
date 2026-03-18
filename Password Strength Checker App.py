import tkinter as tk
from tkinter import ttk

def check_password_strength():
    """
    Checks the strength of the password based on its length and updates the label.
    """
    password = password_entry.get()
    length = len(password)
    
    if length == 0:
        strength_label.config(text="Please enter a password", foreground="black")
        progress_bar['value'] = 0
    elif length < 6:
        strength_label.config(text="Weak: Length < 6 characters", foreground="red")
        progress_bar['value'] = 25
    elif length < 10:
        strength_label.config(text="Moderate: Length >= 6 and < 10", foreground="orange")
        progress_bar['value'] = 50
    elif length < 14:
        strength_label.config(text="Strong: Length >= 10 and < 14", foreground="blue")
        progress_bar['value'] = 75
    else:
        strength_label.config(text="Very Strong: Length >= 14 characters", foreground="green")
        progress_bar['value'] = 100

# --- Set up the main application window ---
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200") # Set the initial size of the window

# Create a main frame for padding
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# --- Widgets ---

# Label for password entry
ttk.Label(main_frame, text="Enter Password:").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))

# Password entry field (shows asterisks)
password_entry = ttk.Entry(main_frame, show="*", width=30)
password_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 10))
# Bind the entry field to the function so it updates as user types
password_entry.bind('<KeyRelease>', lambda event: check_password_strength())

# Label to display strength result
strength_label = ttk.Label(main_frame, text="Please enter a password", foreground="black")
strength_label.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))

# Progress bar to visually show strength
progress_bar = ttk.Progressbar(main_frame, orient='horizontal', length=300, mode='determinate')
progress_bar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))

# Configure the grid to resize nicely
main_frame.columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()