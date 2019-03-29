import tkinter

from .button_link import ButtonLink
from .issues_and_pull_requests import IssuesAndPullRequests
from .utils import pluralize
from . import grid


class Details(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.repositories = []

        self.name = ButtonLink(self, text='', href='')
        self.summary = tkinter.Label(self, text='')

        self.notebook = IssuesAndPullRequests(self)

        self.name.grid(row=0, column=0, sticky='nsew')
        self.summary.grid(row=1, column=0, sticky='nsew')
        self.notebook.grid(row=2, column=0, sticky='nsew')

        grid.weight_row(self, 0, weight=0)
        grid.weight_row(self, 1, weight=0)
        grid.weight_row(self, 2, weight=1)
        grid.weight_col(self, 0, weight=1)

    def populate(self, repositories):
        self.repositories = repositories

    def select_repo(self, index):
        print('Selected repository index #{}.'.format(index))

        data = self.repositories[index]
        issues = data['issues']['nodes']
        pull_requests = data['pullRequests']['nodes']

        name = data['nameWithOwner']
        repo_url = data['url']

        summary = '{}, {}.'.format(
            pluralize(len(issues), 'issue'),
            pluralize(len(pull_requests), 'pull request'),
        )

        self.name.config(text=name)
        self.name.href = repo_url
        self.summary.config(text=summary)
        self.notebook.populate(data)
