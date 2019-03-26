import tkinter
from .utils import pluralize

class Details(tkinter.Frame):
    def __init__(self, root, parent, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.parent = parent
        self.ghi = ghi

        self.name = tkinter.Label(text='')
        self.summary = tkinter.Label(text='')

    def select_repo(self, index, repo):
        print('details.select_repo({}, {})'.format(index, repo))

        data = self.ghi.repositories()[index]
        issues = data['issues']['nodes']
        pull_requests = data['pullRequests']['nodes']

        name = repo
        summary = '{}, {}.'.format(
            pluralize(len(issues), 'issue'),
            pluralize(len(pull_requests), 'pull request'),
        )

        self.name.config(text=name)
        self.summary.config(text=summary)
        from pprint import pprint
        pprint(self.ghi.repositories()[index])
