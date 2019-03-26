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
        self.repo_list = RepoList(self, self.ghi)
        self.details = Details(self, self.ghi)

        self.repo_list.grid(row=0, column=0)
        self.details.grid(row=0, column=1)

    def run(self):
        self.grid(row=0, column=0)
        self.repo_list.populate()
        self.repo_list.select(0)
        self.details.notebook.issues.select(0)
        #self.details.notebook.pull_requests.select(0)
        self.root.mainloop()


def main(args=None):
    """Start ghi's GUI."""
    return Gui().run()
