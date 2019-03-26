import tkinter

class Details(tkinter.Frame):
    def __init__(self, root, parent, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.parent = parent
        self.ghi = ghi

        self.name = tkinter.Label(text='')
        self.name.grid(row=0, column=1)

        self.summary = tkinter.Label(text='')
        self.summary.grid(row=1, column=1)

    def select_repo(self, index, repo):
        print('details.select_repo({}, {})'.format(index, repo))

        data = self.ghi.repositories()[index]
        issues = data['issues']['nodes']
        pull_requests = data['pullRequests']['nodes']

        name = repo
        summary = '{} issues, {} pull requests.'.format(
            len(issues),
            len(pull_requests)
        )

        self.name.config(text=name)
        self.summary.config(text=summary)
        from pprint import pprint
        pprint(self.ghi.repositories()[index])
