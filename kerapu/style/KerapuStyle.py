"""
PyStratum

Copyright 2015-2016 Set Based IT Consultancy

Licence MIT
"""
from cleo import OutputFormatterStyle
from cleo.styles import CleoStyle


class KerapuStyle(CleoStyle):
    """
    Output style for Kerapu.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, input, output):
        """
        Object constructor.

        :param cleo.inputs.input.Input input: The input object.
        :param cleo.outputs.output.Output output: The output object.
        """
        CleoStyle.__init__(self, input, output)

        # Create style notes.
        style = OutputFormatterStyle('yellow', None, ['bold'])
        output.get_formatter().set_style('note', style)

        # Create style for file and directory names.
        style = OutputFormatterStyle('white', None, ['bold'])
        output.get_formatter().set_style('fso', style)

    # ------------------------------------------------------------------------------------------------------------------
    def text(self, message):
        if isinstance(message, list):
            messages = message
        else:
            messages = [message]

        for line in messages:
            self.writeln(' {0}'.format(line))

# ----------------------------------------------------------------------------------------------------------------------
