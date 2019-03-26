import tkinter
from tkinter import tix

from .. import Ghi
from .repo_list import RepoList
from .details import Details


class Gui(tkinter.Frame):
    def __init__(self, root=None):
        if root is None:
            root = tix.Tk()
        super().__init__(root)

        self.root = root
        self.repo_list = RepoList(self)
        self.details = Details(self)

        self.repo_list.grid(row=0, column=0)
        self.details.grid(row=0, column=1)

        self.grid(row=0, column=0)

    def populate(self):
        ghi = Ghi()
        repos = ghi.repositories()
        self.details.populate(repos)
        self.repo_list.populate(repos)

    def run(self):
        self.populate()
        self.root.mainloop()


def main(args=None):
    """Start ghi's GUI."""
    return Gui().run()
