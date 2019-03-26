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

        self.ghi = Ghi()
        self.root = root
        self.repo_list = RepoList(self.root, self, self.ghi)
        self.details = Details(self.root, self, self.ghi)

    def arrange(self):
        self.repo_list.repos.grid(row=0, column=0, rowspan=2)
        self.details.name.grid(row=0, column=1)
        self.details.summary.grid(row=1, column=1)

    def run(self):
        self.repo_list.populate()
        self.repo_list.select(0)
        self.arrange()
        self.root.mainloop()


def main(args=None):
    """Start ghi's GUI."""
    return Gui().run()
