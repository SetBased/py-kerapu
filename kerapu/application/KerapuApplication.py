"""
Kerapu
"""
from typing import List

from cleo import Application, Command

from kerapu.command.ShredderCommand import ShredderCommand
from kerapu.command.TestsetShredderCommand import TestShredderCommand


class KerapuApplication(Application):
    """
    The Kerapu application.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Object constructor.
        """
        Application.__init__(self, 'kerapu', '2.0.1')

    # ------------------------------------------------------------------------------------------------------------------
    def get_default_commands(self) -> List[Command]:
        """
        Returns the default commands of this application.

        :rtype: list[Command]
        """
        commands = Application.get_default_commands(self)

        # Kerapu:
        commands.append(ShredderCommand())
        commands.append(TestShredderCommand())

        return commands

# ----------------------------------------------------------------------------------------------------------------------
