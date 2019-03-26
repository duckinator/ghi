import tkinter
from tkinter import tix

from .button_link import ButtonLink
from .utils import pluralize

class Issues(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root

        self.scrolled_listbox = tix.ScrolledListBox(self, width=0, height=0)
        self.listbox = self.scrolled_listbox.listbox
        self.listbox.bind('<<ListboxSelect>>', self.select_callback)

        self.scrolled_listbox.grid(row=0, column=0)

    def select(self, index):
        # Select item +index+.
        self.listbox.select_set(index)
        self.listbox.event_generate('<<ListboxSelect>>')

    def select_callback(self, event):
        widget = event.widget
        selection = widget.curselection()

        if len(selection) == 0:
            return

        index = int(selection[0])
        self._select_callback(widget, index)

    def populate(self, repo_data):
        self._issues = repo_data['issues']['nodes']

        # FIXME: Actually determine the number to delete.
        self.listbox.delete(0, 999999999)

        biggest = max(map(lambda issue: issue['number'], self._issues))
        zero_pad = len(str(biggest))

        print('Populating issues:')
        for issue in self._issues:
            issue_number = str(issue['number']).zfill(zero_pad)
            item = ('#{} - {}').format(issue_number, issue['title'])
            print('- {}'.format(item))
            self.listbox.insert('end', item)
        print('Done.')

        self.select(0)

    def _select_callback(self, widget, index):
        value = widget.get(index)
        print('Selected issue: {} {}'.format(index, value))
