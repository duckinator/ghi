import tkinter
from tkinter import tix

from .. import Ghi
from .repo_list import RepoList
from .details import Details

from . import window
from . import utils


class Gui(tkinter.Frame):
    def __init__(self, root=None):
        if root is None:
            root = tix.Tk()
        super().__init__(root)

        window.load_state(root.winfo_toplevel())
        root.bind('<Configure>', self.on_configure)

        self.root = root
        self.repo_list = RepoList(self)
        self.details = Details(self)

        self.repo_list.grid(row=0, column=0, sticky='nsew')
        self.details.grid(row=0, column=1, sticky='nsew')

        self.grid(row=0, column=0, sticky='nsew')

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

    def populate(self):
        ghi = Ghi()
        repos = ghi.repositories()
        self.details.populate(repos)
        self.repo_list.populate(repos)

        repo_list_width = utils.listbox_width(ghi.repository_names())
        print("Repo List Width = {}".format(repo_list_width))
        self.repo_list.listbox.config(width=repo_list_width)

    def run(self):
        self.populate()
        self.root.mainloop()

    def on_configure(self, _event):
        window.save_state(self.root.winfo_toplevel())


def main():
    """Start ghi's GUI."""
    return Gui().run()
