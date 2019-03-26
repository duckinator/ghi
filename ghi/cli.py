"""Command-line interface.
"""
from argparse import ArgumentParser, SUPPRESS
from . import Ghi

class Cli:
    def __init__(self):
        self.ghi = Ghi()

    def print_rate_limit(self):
        for (key, val) in self.ghi.rate_limit.items():
            print("{}={}".format(key, val))

    @staticmethod
    def print_repo_summaries(repos):
        for repo in repos:
            print('- {} ({} issues, {} PRs)'.format(
                repo['nameWithOwner'],
                len(repo['issues']['nodes']),
                len(repo['pullRequests']['nodes'])))

    def run(self):
        self.ghi.fetch_data()
        print('Username: {}'.format(self.ghi.github_username()))
        print('Repositories:')
        self.print_repo_summaries(self.ghi.repositories())


def main(args=None):
    """Invoke ghi from command-line arguments.
    """
    return Cli().run()
