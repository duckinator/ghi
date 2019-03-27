from .issues import IssueList
from .issues import Issues


class PullRequestList(IssueList):
    _populate_key = 'pullRequests'


class PullRequests(Issues):
    _list_class = PullRequestList
