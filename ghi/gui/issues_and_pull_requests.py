import tkinter
from tkinter import ttk

from .issues import Issues
from .button_link import ButtonLink
from .utils import pluralize

class IssuesAndPullRequests(ttk.Notebook):
    def __init__(self, root, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.ghi = ghi

        self.issues = Issues(self, ghi)
        #self.pull_requests = PullRequets(self, ghi)
        self.pull_requests = tkinter.Frame(self)

        self.add(self.issues, text='Issues')
        self.add(self.pull_requests, text='Pull Requests')

    def populate(self, repo_data):
        self.issues.populate(repo_data)
        #self.pull_requests.populate(repo_data)
