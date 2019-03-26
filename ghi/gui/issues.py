import tkinter
from tkinter import tix

from .ghi_listbox import GhiListbox
from .button_link import ButtonLink
from .utils import pluralize

class Issues(GhiListbox):
    def _populate(self, repo_data):
        self._issues = repo_data['issues']['nodes']

        biggest = max(map(lambda issue: issue['number'], self._issues))
        zero_pad = len(str(biggest))

        print('Populating issues:')
        for issue in self._issues:
            issue_number = str(issue['number']).zfill(zero_pad)
            item = ('#{} - {}').format(issue_number, issue['title'])
            print('- {}'.format(item))
            self.listbox.insert('end', item)
        print('Done.')

    def _select_callback(self, widget, index):
        value = widget.get(index)
        print('Selected issue: {} {}'.format(index, value))
