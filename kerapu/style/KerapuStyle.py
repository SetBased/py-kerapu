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
    def __init__(self, input_object: Input, output_object: Output) -> None:
        """
        Object constructor.

        :param Input input_object: The input object.
        :param Output output_object: The output object.
        """
        CleoStyle.__init__(self, input_object, output_object)

        # Create style notes.
        output_object.get_formatter().add_style('note', 'yellow', None, ['bold'])

        # Create style for file and directory names.
        output_object.get_formatter().add_style('fso', 'white', None, ['bold'])

    # ------------------------------------------------------------------------------------------------------------------
    def text(self, message: Union[str, list, None]) -> None:
        if isinstance(message, list):
            messages = message
        else:
            messages = [message]

        for line in messages:
            self.writeln(' {0}'.format(line))

# ----------------------------------------------------------------------------------------------------------------------
