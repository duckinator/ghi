import tkinter

from .button_link import ButtonLink
from .ghi_listbox import GhiListbox
from . import grid
from . import utils


class IssueList(GhiListbox):
    _populate_key = 'issues'

    def _populate(self, repo_data):
        self._data = repo_data[self._populate_key]['nodes']

        if len(self._data) == 0:
            print('No {} data.'.format(self._populate_key))
            return

        # Determine the highest issue number.
        biggest = max(map(lambda issue: issue['number'], self._data))
        # Calculate the length of +biggest+.
        zero_pad = len(str(biggest))

        # Automagically resize the listbox to fit the longest name.
        names = map(lambda obj: obj['title'], self._data)
        width = utils.listbox_width(names, max_width=60)
        self.listbox.config(width=width)

        # Populate the listbox.
        print('Populating {}.'.format(self._populate_key))
        for issue in self._data:
            issue_number = str(issue['number']).zfill(zero_pad)
            item = ('#{} - {}').format(issue_number, issue['title'])
            self.listbox.insert('end', item)

    def _select_callback(self, _widget, index):
        self.root.details.populate(self._data[index])


class IssueDetails(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.title = ButtonLink(self, text='', href='')
        self.body = tkinter.Label(self, text='')
        self.title.grid(row=0, column=0, sticky='nsew')
        self.body.grid(row=1, column=0, sticky='nsew')

        grid.weight_row(self, 0, weight=0)
        grid.weight_row(self, 1, weight=1)
        grid.weight_col(self, 0, weight=1)

    def populate(self, issue):
        title = '#{} - {}'.format(issue['number'], issue['title'])
        self.title.configure(text=title)
        self.title.href = issue['url']
        self.body.configure(text=issue['body'])


class Issues(tkinter.Frame):
    _list_class = IssueList
    _details_class = IssueDetails

    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.list = self._list_class(self)
        self.details = self._details_class(self)
        self.list.grid(row=0, column=0, sticky='nsew')
        self.details.grid(row=0, column=1, sticky='nsew')

        grid.weight_row(self, 0, weight=1)
        grid.weight_col(self, 1, weight=1)

    def populate(self, *args, **kwargs):
        self.list.populate(*args, **kwargs)
