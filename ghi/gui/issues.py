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
        self.root.update_data(self._data[index])


class Issues(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.list = self.build_list()

        self.title = ButtonLink(self, text='', href='')
        self.body = tkinter.Label(self, text='')

        self.list.grid(row=0, column=0, rowspan=2, sticky='nsew')
        self.title.grid(row=0, column=1, sticky='nsew')
        self.body.grid(row=1, column=1, sticky='nsew')

        grid.weight(self, 0, 0, weight=0)
        grid.weight(self, 1, 1, weight=0)
        grid.weight(self, 2, 1, weight=1)

    def build_list(self):
        return IssueList(self)

    def populate(self, *args, **kwargs):
        self.list.populate(*args, **kwargs)

    def update_data(self, issue):
        title = '#{} - {}'.format(issue['number'], issue['title'])
        self.title.configure(text=title)
        self.title.href = issue['url']
        self.body.configure(text=issue['body'])
