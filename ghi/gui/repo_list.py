import tkinter
from tkinter import tix

class RepoList(tkinter.Frame):
    def __init__(self, root, parent, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.parent = parent
        self.ghi = ghi

        self.repos = tix.ScrolledListBox(self.root, width=0, height=0)
        # FIXME: Make self.repos fill all rows!
        self.repos.grid(row=0, column=0, rowspan=2)

        self.add_event_handlers()

    def select(self, n):
        # Select item +n+.
        self.repos.listbox.select_set(n)
        self.repos.listbox.event_generate('<<ListboxSelect>>')

    def populate(self):
        print('Populating repository list.')
        for repo in self.ghi.repositories():
            self.repos.listbox.insert('end', repo['nameWithOwner'])

    def select_repo(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        self.parent.details.select_repo(index, value)

    def add_event_handlers(self):
        print('Adding event handlers.')
        self.repos.listbox.bind('<<ListboxSelect>>', self.select_repo)
