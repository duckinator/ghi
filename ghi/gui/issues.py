import tkinter
from tkinter import tix

from .ghi_listbox import GhiListbox
from .button_link import ButtonLink
from .utils import pluralize

class Issues(GhiListbox):
    def _populate(self, repo_data, key='issues'):
        self._data = repo_data[key]['nodes']

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
        value = widget.get(index)
        print('Selected issue: {} {}'.format(index, value))
