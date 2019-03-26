"""GUI for Ghi."""
import sys
import tkinter as tk
from tkinter import tix
from . import Ghi

class Details(tk.Frame):
    def __init__(self, root, parent, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.parent = parent
        self.ghi = ghi
        self.summary = tk.Label(text="awoo")
        self.summary.grid(row=0, column=1)

    def select_repo(self, index, repo):
        print("Details.select_repo: {} {}".format(index, repo))
        self.summary.config(text=repo)


class RepoList(tk.Frame):
    def __init__(self, root, parent, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.parent = parent
        self.ghi = ghi

        self.repos = tix.ScrolledListBox(self.root, width=0, height=0)
        self.repos.grid(row=0, column=0)

        self.add_event_handlers()

    def select(self, n):
        # Select item +n+.
        self.repos.listbox.select_set(n)
        self.repos.listbox.event_generate("<<ListboxSelect>>")

    def populate(self):
        print("Populating repository list.")
        for repo in self.ghi.repositories():
            self.repos.listbox.insert('end', repo['nameWithOwner'])

    def select_repo(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        self.parent.details.select_repo(index, value)

    def add_event_handlers(self):
        print("Adding event handlers.")
        self.repos.listbox.bind('<<ListboxSelect>>', self.select_repo)


class Gui(tk.Frame):
    def __init__(self, root=None):
        if root is None:
            root = tix.Tk()
        super().__init__(root)

        self.ghi = Ghi()
        self.root = root
        self.repo_list = RepoList(self.root, self, self.ghi)
        self.details = Details(self.root, self, self.ghi)

    def run(self):
        self.repo_list.populate()
        self.repo_list.select(0)
        self.root.mainloop()

def main(args=None):
    """Start ghi's GUI."""
    return Gui().run()
