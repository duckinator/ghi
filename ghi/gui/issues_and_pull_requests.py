from tkinter import ttk

from .issues import Issues
from .pull_requests import PullRequests


class IssuesAndPullRequests(ttk.Notebook):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.issues = Issues(self)
        self.pull_requests = PullRequests(self)

        self.add(self.issues, text='Issues')
        self.add(self.pull_requests, text='Pull Requests')

    def populate(self, repo_data):
        self.issues.populate(repo_data)
        self.pull_requests.populate(repo_data)
