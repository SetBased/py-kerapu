"""
Kerapu
"""
from kerapu.application.KerapuApplication import KerapuApplication


def main():
    """
    Entry point for the kerapu console script.
    """
    application = KerapuApplication()
    status = application.run()

    exit(status)
