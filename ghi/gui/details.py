import tkinter

from .button_link import ButtonLink
from .issues_and_pull_requests import IssuesAndPullRequests
from .utils import pluralize

class Details(tkinter.Frame):
    def __init__(self, root, parent, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.parent = parent
        self.ghi = ghi

        self.name = ButtonLink(root, text='', href='')
        self.summary = tkinter.Label(text='')

        #self.notebook = IssuesAndPullRequests(self, ghi)
        self.notebook = IssuesAndPullRequests(root, ghi)

    def select_repo(self, index):
        print('details.select_repo({})'.format(index))

        data = self.ghi.repositories()[index]
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
        from pprint import pprint
        pprint(self.ghi.repositories()[index])
