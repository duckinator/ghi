import tkinter
from tkinter import tix

from .button_link import ButtonLink
from .utils import pluralize

class Issues(tkinter.Frame):
    def __init__(self, root, ghi):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.ghi = ghi

        self.scrolled_listbox = tix.ScrolledListBox(self, width=0, height=0)
        self.listbox = self.scrolled_listbox.listbox
        self.listbox.bind('<<ListboxSelect>>', self.select_callback)

        self.scrolled_listbox.grid(row=0, column=0)

    def populate(self, repo_data):
        self._issues = repo_data['issues']['nodes']

        # This clears _all_ items in the listbox.
        self.listbox.delete(0)

        zero_pad = len(str(len(self._issues)))
        print('zero_pad={}'.format(zero_pad))

        print('Populating issues:')
        for issue in self._issues:
            # FIXME: Include issue number in data.
            issue_number = issue['url'].split('/')[-1]
            issue_number = str(issue_number).zfill(zero_pad)
            item = ('{} {}').format(issue_number, issue['title'])
            print('- {}'.format(item))
            self.listbox.insert('end', item)
        print('Done.')

        # TODO: Check if theres >0 issues before calling .select(0).
        self.select(0)

    def select(self, n):
        # Select item +n+.
        self.listbox.select_set(n)
        self.listbox.event_generate('<<ListboxSelect>>')

    def select_callback(self, event):
        widget = event.widget
        print(widget.curselection())
        #index = int(widget.curselection()[0])
        #value = widget.get(index)
        #print('Selected issue: {} {}'.format(index, value))
