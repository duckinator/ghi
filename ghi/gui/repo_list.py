from .ghi_listbox import GhiListbox


class RepoList(GhiListbox):
    def _populate(self, repositories):
        print('Populating repository list.')
        for repo in repositories:
            self.listbox.insert('end', repo['nameWithOwner'])

    def _select_callback(self, _widget, index):
        self.root.details.select_repo(index)
