from .issues import Issues

class PullRequests(Issues):
    def _populate(self, repo_data):
        super()._populate(repo_data, key='pullRequests')

    def _select_callback(self, widget, index):
        value = widget.get(index)
        print('Selected PR: {} {}'.format(index, value))
