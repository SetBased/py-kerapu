"""
PyStratum
"""
from typing import Union

from cleo import Input, Output
from cleo.styles import CleoStyle


class KerapuStyle(CleoStyle):
    """
    Output style for Kerapu.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, input: Input, output: Output):
        """
        Object constructor.

        :param Input input: The input object.
        :param Output output: The output object.
        """
        CleoStyle.__init__(self, input, output)

        # Create style notes.
        output.get_formatter().add_style('note', 'yellow', None, ['bold'])

        # Create style for file and directory names.
        output.get_formatter().add_style('fso', 'white', None, ['bold'])

    # ------------------------------------------------------------------------------------------------------------------
    def text(self, message: Union[str, list, None]):
        if isinstance(message, list):
            messages = message
        else:
            messages = [message]

        for line in messages:
            self.writeln(' {0}'.format(line))

# ----------------------------------------------------------------------------------------------------------------------
