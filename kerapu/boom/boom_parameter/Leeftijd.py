"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class Leeftijd(BoomParameter):
    """
    Klasse voor boomparameter leeftijd.

    Boomparameternummer: 100.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, leeg, subtraject: Subtraject) -> int:
        """
        Geeft de leeftijd van de patient van een subtraject.

        :param None leeg: Wordt niet gebruikt.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.leeftijd

# ----------------------------------------------------------------------------------------------------------------------
