import tkinter
from tkinter import ttk

from .issues import Issues
from .pull_requests import PullRequests
from . import grid


class IssuesAndPullRequests(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky='nsew')
        grid.weight_row(self, 0, weight=1)
        grid.weight_col(self, 0, weight=1)

        self.issues = Issues(self)
        self.pull_requests = PullRequests(self)

        self.notebook.add(self.issues, text='Issues')
        self.notebook.add(self.pull_requests, text='Pull Requests')

    def populate(self, repo_data):
        self.issues.populate(repo_data)
        self.pull_requests.populate(repo_data)
