import tkinter
from tkinter import tix

class RepoList(tkinter.Frame):
    def __init__(self, root, parent, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.parent = parent
        self.ghi = ghi
        self.repos = tix.ScrolledListBox(self.root, width=0, height=0)
        self.repos.listbox.bind('<<ListboxSelect>>', self.select_callback)

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
        print(widget)

        index = int(widget.curselection()[0])
        self.parent.details.select_repo(index)
