"""Github-Human Interface

Ghi is a tool for making the management of issues and PRs across a large
number of projects simpler.
"""
import itertools
from pathlib import Path
from . import config
from . import graphql


class Ghi:
    """"Provides the core functionality of Ghi.
    """

    query = Path(__file__).with_name('query.graphql').read_text()

    def __init__(self):
        self.data = None
        self.rate_limit = None
        self._repositories = None
        self.viewer = None

    def fetch_data(self):
        if self.data is not None:
            return

        self.data = graphql.request(self.query)['data']
        self.rate_limit = self.data['rateLimit']
        self.viewer = self.data['viewer']

    def github_username(self):
        return self.viewer['login']

    def _user_repos(self):
        return self.viewer['repositories']['nodes']

    def _org_repos(self):
        repos = map(lambda x: x['repositories']['nodes'],
                    self.viewer['organizations']['nodes'])
        return list(itertools.chain.from_iterable(repos))

    @staticmethod
    def _repo_is_ignored(repo):
        return repo['nameWithOwner'] in config.ignored()

    def _repo_is_relevant(self, repo):
        archived = repo['isArchived']
        has_issues = len(repo['issues']['nodes']) > 0
        has_prs = len(repo['pullRequests']['nodes']) > 0

        return (not archived) \
            and (has_issues or has_prs) \
            and (not self._repo_is_ignored(repo))

    @staticmethod
    def _repo_name(repo):
        return repo['nameWithOwner']

    def repositories(self):
        if self._repositories is not None:
            return self._repositories

        repos = self._user_repos() + self._org_repos()
        repos = filter(self._repo_is_relevant, repos)
        self._repositories = sorted(repos, key=self._repo_name)
        return self._repositories
