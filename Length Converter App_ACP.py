import tkinter as tk
from tkinter import ttk

def convert_length():
    """Converts the input inches value to centimeters and updates the result label."""
    try:
        inches = float(inches_entry.get())
        # 1 inch = 2.54 centimeters
        centimeters = inches * 2.54
        # Update the result label with the calculated value, rounded to two decimal places
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        # Handle invalid input (non-numeric)
        result_label.config(text="Invalid Input")

# --- Set up the main application window ---
root = tk.Tk()
root.title("Inches to Centimeters Converter")
# Set a minimum size for the window
root.geometry("300x300")

# --- Create and place the widgets ---

# Input Label and Entry box
inches_label = ttk.Label(root, text="Enter length in Inches:")
inches_label.pack(pady=10)

inches_entry = ttk.Entry(root, width=15)
inches_entry.pack(pady=5)
inches_entry.focus_set() # Set focus to the entry box on startup

# Convert Button
convert_button = ttk.Button(root, text="Convert", command=convert_length)
convert_button.pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="Result: 0.00 cm", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

# --- Start the Tkinter event loop ---
root.mainloop()