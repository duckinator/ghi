"""GUI for Ghi."""
import sys
from tkinter import tix
from . import Ghi

class Gui:
    def __init__(self):
        self.ghi = Ghi()
        self.root = tix.Tk()
        self.repos = tix.ScrolledListBox(self.root, name='repos')
        self.details = tix.ScrolledText(self.root)

    def debug(self):
        import code
        code.interact(local=locals())

    def populate_repos(self):
        print("Populating repos.")
        for repo in self.ghi.repositories():
            self.repos.listbox.insert('end', repo['nameWithOwner'])

    def populate(self):
        self.populate_repos()

    def arrange(self):
        print("Arranging widgets.")
        self.repos.grid(row=0, column=0)
        self.details.grid(row=0, column=1)

    def select_repo(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        print("Selected {}: {}".format(index, value))

    def add_event_handlers(self):
        print("Adding event handlers.")
        self.repos.listbox.bind('<<ListboxSelect>>', self.select_repo)

    def run(self):
        self.arrange()
        self.populate()
        self.add_event_handlers()
        if '--debug' in sys.argv:
            print("Entering debugger.")
            self.debug()
        else:
            print("Running main loop.")
            self.root.mainloop()

def main(args=None):
    """Start ghi's GUI."""
    return Gui().run()
