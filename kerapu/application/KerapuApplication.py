"""
Kerapu
"""
from cleo import Application

from kerapu.command.ShredderCommand import ShredderCommand


class KerapuApplication(Application):
    """
    The Kerapu application.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        Application.__init__(self, 'kerapu', '1.0.1')

    # ------------------------------------------------------------------------------------------------------------------
    def get_default_commands(self):
        """
        Returns the default commands of this application.

        :rtype: list[cleo.Command]
        """
        commands = Application.get_default_commands(self)

        # Kerapu:
        commands.append(ShredderCommand())

        return commands

# ----------------------------------------------------------------------------------------------------------------------
