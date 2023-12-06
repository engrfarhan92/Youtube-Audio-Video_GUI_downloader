from tkinter import *

root = Tk()

def popup(event):
    try:
        menu.tk_popup(event.x_root,event.y_root) # Pop the menu up in the given coordinates
    finally:
        menu.grab_release() # Release it once an option is selected

def paste():
    clipboard = root.clipboard_get() # Get the copied item from system clipboardem clipboar
    e.insert('end',clipboard) # Insert the item into the entry widget

def copy():
    inp = e.get() # Get the text inside entry widget
    root.clipboard_clear() # Clear the tkinter clipboard
    root.clipboard_append(inp) # Append to system clipboard

menu = Menu(root,tearoff=0) # Create a menu
menu.add_command(label='Copy',command=copy) # Create labels and commands
menu.add_command(label='Paste',command=paste)

e = Entry(root) # Create an entry
e.pack(padx=10,pady=10)

e.bind('<Button-3>',popup) # Bind a func to right click

root.mainloop()