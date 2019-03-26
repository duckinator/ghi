import tkinter
from tkinter import tix

from . import grid

class GhiListbox(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self._data = None

        self.scrolled_listbox = tix.ScrolledListBox(self, width=0, height=0)
        self.listbox = self.scrolled_listbox.listbox
        self.listbox.bind('<<ListboxSelect>>', self.select_callback)

        self.scrolled_listbox.grid(row=0, column=0, sticky='nsew')
        grid.weight(self, [0], [0])

    def select(self, index):
        # Select item +index+.
        self.listbox.select_set(index)
        self.listbox.event_generate('<<ListboxSelect>>')

    def select_callback(self, event):
        widget = event.widget
        selection = widget.curselection()

        if len(selection) == 0:
            return

        index = int(selection[0])
        self._select_callback(widget, index)

    def populate(self, data):
        # FIXME: Actually determine the number to delete.
        self.listbox.delete(0, 999999999)
        self._populate(data)
        self.select(0)

    def _populate(_self, _repo_data):
        raise NotImplementedError

    def _select_callback(_self, _widget, _index):
        raise NotImplementedError
