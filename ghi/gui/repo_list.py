import tkinter
from tkinter import tix

class RepoList(tkinter.Frame):
    def __init__(self, root, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.ghi = ghi
        self.repos = tix.ScrolledListBox(self, width=0, height=0)
        self.repos.listbox.bind('<<ListboxSelect>>', self.select_callback)

        self.repos.grid(row=0, column=0)

    def select(self, index):
        # Select item +index+.
        self.repos.listbox.select_set(index)
        self.repos.listbox.event_generate('<<ListboxSelect>>')

    def populate(self):
        print('Populating repository list.')
        for repo in self.ghi.repositories():
            self.repos.listbox.insert('end', repo['nameWithOwner'])

    def select_callback(self, event):
        widget = event.widget
        selection = widget.curselection()

        if len(selection) == 0:
            return

        index = int(selection[0])
        self.root.details.select_repo(index)
