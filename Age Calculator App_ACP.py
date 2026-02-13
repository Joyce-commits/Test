import tkinter as tk
from datetime import date
from tkinter import ttk, messagebox

def calculate_age():
    """Calculates age based on user input and displays it."""
    try:
        # Get input from spinboxes and convert to integers
        day = int(day_var.get())
        month = int(month_var.get())
        year = int(year_var.get())
        
        # Create a date object for the date of birth
        dob = date(year, month, day)
        today = date.today()
        
        # Calculate the difference in years
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        # Display the result in the label
        result_label.config(text=f"Your present age is: {age} years")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid date, month, and year values.")
    except Exception as e:
        messagebox.showerror("An Error Occurred", f"An unexpected error occurred: {e}")

# --- Tkinter GUI Setup ---

# Create the main window
app = tk.Tk()
app.title("Age Calculator")
app.geometry("350x250")

# Use a themed style for better aesthetics
style = ttk.Style(app)
style.configure("TLabel", padding=5)
style.configure("TButton", padding=5)

# Create input frame
input_frame = ttk.Frame(app, padding="10 10 10 10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and Spinboxes for date input

# Day
ttk.Label(input_frame, text="Day:").grid(row=0, column=0, sticky=tk.W)
day_var = tk.StringVar(value='1')
day_spinbox = tk.Spinbox(input_frame, from_=1, to_=31, width=5, textvariable=day_var)
day_spinbox.grid(row=0, column=1, sticky=tk.E)

# Month
ttk.Label(input_frame, text="Month:").grid(row=1, column=0, sticky=tk.W)
month_var = tk.StringVar(value='1')
month_spinbox = tk.Spinbox(input_frame, from_=1, to_=12, width=5, textvariable=month_var)
month_spinbox.grid(row=1, column=1, sticky=tk.E)

# Year
ttk.Label(input_frame, text="Year:").grid(row=2, column=0, sticky=tk.W)
year_var = tk.StringVar(value='2000')
# Set the range for year dynamically, for example, from 1900 to the current year
current_year = date.today().year
year_spinbox = tk.Spinbox(input_frame, from_=1900, to_=current_year, width=5, textvariable=year_var)
year_spinbox.grid(row=2, column=1, sticky=tk.E)

# Calculate button
calculate_button = ttk.Button(app, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=1, column=0, pady=10)

# Result label
result_label = ttk.Label(app, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, pady=10)

# Start the Tkinter event loop
app.mainloop()