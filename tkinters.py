import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext

root = tk.Tk()
root.title("Calculator")

root.maxsize()

buttons = []
for i in range(2, 7):
    button_row = []
    for j in range(2, 5):
        button = tk.Button(root, text='', width=20, height=10)
        button.grid(row=j, column=i)
        button_row.append(button)
    buttons.append(button_row)
#
# Create a scrolled text widget for displaying the archive
archive_text = scrolledtext.ScrolledText(root, width=30, height=10)
archive_text.grid(row=0, column=0)

root.mainloop()

""" Creating an application window: first line: root = tk.tk(), last line: root.mainloop()"""
