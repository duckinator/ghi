"""Command-line interface.
"""
from argparse import ArgumentParser, SUPPRESS
from . import Ghi


def _parse_args(args):
    argparser = ArgumentParser(
        description="Make managing GitHub issues/PRs easier.",
        argument_default=SUPPRESS,
    )

    # There's no actual command-line arguments.
    # I just figured I'd include the plumbing for it before it was needed.
    # -@duckinator

    return argparser.parse_args(args)


def main(args=None):
    """Invoke ghi from command-line arguments.
    """
    args = _parse_args(args)

    return Ghi(args).run()
