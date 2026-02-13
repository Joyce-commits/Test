import tkinter as tk
from tkinter import messagebox

def calculate_product():
    """Calculates the product of the two numbers entered by the user."""
    try:
        # Get the numbers from the input fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Calculate the product
        product = num1 * num2

        # Display the result
        result_var.set(f"Product: {product}")
    except ValueError:
        # Show an error message if the input is not a valid number
        messagebox.showerror("Invalid input", "Please enter valid numbers in both fields.")

# --- Main Tkinter window setup ---
root = tk.Tk()
root.title("Product Calculator")

# Optional: set a minimum size for the window
root.geometry("300x200")

# --- Widgets ---

# Label and Entry for the first number
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

# Label and Entry for the second number
label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.pack(pady=10)

# Label to display the result
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

# --- Start the Tkinter event loop ---
root.mainloop()