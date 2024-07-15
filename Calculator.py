#!/usr/bin/env python
# coding: utf-8

# # Tkinter_Calculator

# In[33]:


import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("CALCULATOR")

# Define colors
bg_color = "#F0F8FF"  # Light Blue for the main frame background
button_bg_color = "#A9A9A9"  # Dark Gray for button backgrounds
button_fg_color = "white"  # White for button text color
border_color = "#808080"  # Medium Gray for border color

# Create a frame to contain the calculator elements with all borders
border_frame = tk.Frame(master=window, bg=border_color, padx=5, pady=5)
border_frame.pack()

# Create the inner frame for calculator elements
frame = tk.Frame(master=border_frame, bg=bg_color, padx=12, pady=12)
frame.pack()

# Entry widget to display input and output
entry = tk.Entry(master=frame, relief=tk.SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

# Function to handle button clicks and insert numbers/operators into entry
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to evaluate the expression and show the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Input")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Define buttons for numbers and operators
buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0", "+", "-",
    "*", "/",  "%",
    "=", "C",  "." ]  # Clear button

# Layout the buttons in the frame using grid
row_num = 1
col_num = 0
for button in buttons:
    if button == "=":
        tk.Button(master=frame, text=button, padx=15, pady=5, width=3, bg="#4682B4", fg=button_fg_color, command=calculate).grid(row=row_num, column=col_num, pady=2)
    elif button == "C":
        tk.Button(master=frame, text=button, padx=15, pady=5, width=3, bg="#4682B4", fg=button_fg_color, command=clear).grid(row=row_num, column=col_num, pady=2)
    else:
        tk.Button(master=frame, text=button, padx=15, pady=5, width=3, bg=button_bg_color, fg=button_fg_color, command=lambda b=button: button_click(b)).grid(row=row_num, column=col_num, pady=2)
    
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1

# Start the main event loop
window.mainloop()


# In[ ]:





# In[ ]:




