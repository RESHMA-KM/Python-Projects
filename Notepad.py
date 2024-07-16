#!/usr/bin/env python
# coding: utf-8

# # Tkinter_Notepad

# In[8]:


import tkinter as tk
from tkinter import Menu, Text, messagebox, filedialog
import os

def create_widgets():
    global text_area, file
    text_area = Text(root)
    text_area.grid(sticky=tk.N+tk.S+tk.E+tk.W)

    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_app)
    menu_bar.add_cascade(label="File", menu=file_menu)

    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About Notepad", command=show_about)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    root.title("Untitled - Notepad")
    file = None

def new_file():
    global file
    root.title("Untitled - Notepad")
    file = None
    text_area.delete(1.0, tk.END)

def open_file():
    global file
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
    if file_path:
        file = file_path
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, tk.END)
        with open(file, "r") as f:
            text_area.insert(1.0, f.read())

def save_file():
    global file
    if file is None:
        file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if file:
            with open(file, "w") as f:
                f.write(text_area.get(1.0, tk.END))
            root.title(os.path.basename(file) + " - Notepad")
    else:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))

def exit_app():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def show_about():
    messagebox.showinfo("About Notepad", "This is a simple Notepad application created using Tkinter.")


root = tk.Tk()
create_widgets()
root.mainloop()


# In[ ]:




