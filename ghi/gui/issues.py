import tkinter
from tkinter import tix
import webbrowser

from .ghi_listbox import GhiListbox
from .button_link import ButtonLink
from .utils import pluralize

class IssueList(GhiListbox):
    def _populate(self, repo_data, key='issues'):
        self._data = repo_data[key]['nodes']

        if len(self._data) == 0:
            print('No {} data.'.format(key))
            return

        biggest = max(map(lambda issue: issue['number'], self._data))
        zero_pad = len(str(biggest))

        print('Populating {}:'.format(key))
        for issue in self._data:
            issue_number = str(issue['number']).zfill(zero_pad)
            item = ('#{} - {}').format(issue_number, issue['title'])
            print('- {}'.format(item))
            self.listbox.insert('end', item)
        print('Done.')

    def _select_callback(self, widget, index):
        self.root.update(self._data[index])

class Issues(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root) # initialize tkinter.Frame.
        self.root = root
        self.list = self.build_list()

        self.title = ButtonLink(self, text='', href='')
        self.body = tkinter.Label(self, text='')

        self.list.grid(row=0, column=0)
        self.title.grid(row=0, column=1)
        self.body.grid(row=1, column=1)

    def build_list(self):
        return IssueList(self)

    def populate(self, *args, **kwargs):
        self.list.populate(*args, **kwargs)

    def update(self, issue):
        title = '#{} - {}'.format(issue['number'], issue['title'])
        self.title.configure(text=title)
        self.title.href = issue['url']
        self.body.configure(text=issue['body'])
