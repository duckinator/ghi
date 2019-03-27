import tkinter

from .button_link import ButtonLink
from .ghi_listbox import GhiListbox
from . import grid


class IssueList(GhiListbox):
    _populate_key = 'issues'

    def _populate(self, repo_data):
        self._data = repo_data[self._populate_key]['nodes']

        if len(self._data) == 0:
            print('No {} data.'.format(self._populate_key))
            return

        biggest = max(map(lambda issue: issue['number'], self._data))
        zero_pad = len(str(biggest))

        print('Populating {}:'.format(self._populate_key))
        for issue in self._data:
            issue_number = str(issue['number']).zfill(zero_pad)
            item = ('#{} - {}').format(issue_number, issue['title'])
            print('- {}'.format(item))
            self.listbox.insert('end', item)
        print('Done.')

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

        grid.weight(self, 0, 0, weight=0)
        grid.weight(self, 1, 0, weight=1)

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

    def populate(self, *args, **kwargs):
        self.list.populate(*args, **kwargs)
