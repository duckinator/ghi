from tkinter import Grid


def weight_col(root, col, weight=1):
    Grid.columnconfigure(root, col, weight=weight)


def weight_row(root, row, weight=1):
    Grid.rowconfigure(root, row, weight=weight)


def weight(root, row, col, weight=1):
    weight_row(root, row, weight)
    weight_col(root, col, weight)
