from tkinter import Grid

def weight(root, row, col, weight=1):
    Grid.rowconfigure(root, row, weight=weight)
    Grid.columnconfigure(root, col, weight=weight)
