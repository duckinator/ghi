import tkinter
from tkinter import ttk

from .issues import Issues
from .button_link import ButtonLink
from .utils import pluralize

class IssuesAndPullRequests(ttk.Notebook):
    def __init__(self, root):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root

        self.issues = Issues(self)
        #self.pull_requests = PullRequets(self)
        self.pull_requests = tkinter.Frame(self)

        self.add(self.issues, text='Issues')
        self.add(self.pull_requests, text='Pull Requests')

    def populate(self, repo_data):
        self.issues.populate(repo_data)
        #self.pull_requests.populate(repo_data)
