import tkinter

from .button_link import ButtonLink
from .issues_and_pull_requests import IssuesAndPullRequests
from .utils import pluralize

class Details(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.repositories = []

        self.name = ButtonLink(self, text='', href='')
        self.summary = tkinter.Label(self, text='')

        self.notebook = IssuesAndPullRequests(self)

        self.name.grid(row=0, column=0)
        self.summary.grid(row=1, column=0)
        self.notebook.grid(row=2, column=0)

    def populate(self, repositories):
        self.repositories = repositories

    def select_repo(self, index):
        print('details.select_repo({})'.format(index))

        data = self.repositories[index]
        issues = data['issues']['nodes']
        pull_requests = data['pullRequests']['nodes']

        name = data['nameWithOwner']
        repo_url = data['url']
        desc = data['shortDescriptionHTML']

        summary = '{}, {}.'.format(
            pluralize(len(issues), 'issue'),
            pluralize(len(pull_requests), 'pull request'),
        )

        self.name.config(text=name)
        self.name.href = repo_url
        self.summary.config(text=summary)
        self.notebook.populate(data)
