import tkinter

class Details(tkinter.Frame):
    def __init__(self, root, parent, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.parent = parent
        self.ghi = ghi
        self.summary = tkinter.Label(text="default value")
        self.summary.grid(row=0, column=1)

    def select_repo(self, index, repo):
        print("details.select_repo({}, {})".format(index, repo))
        self.summary.config(text=repo)
