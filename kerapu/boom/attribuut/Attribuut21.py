"""
Kerapu
"""
from kerapu.boom.attribuut.Attribuut import Attribuut
from kerapu.lbz.Subtraject import Subtraject


class Attribuut21(Attribuut):
    """
    Klasse voor attributen met toetswijze 2 (tussen) en waarde type 1 (numeriek).
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 attribuut_id: int,
                 boom_parameter_nummer: int,
                 onder_filter_waarde: int,
                 boven_filter_waarde: int):
        """
        Object constructor.

        :param int attribuut_id: Het ID van dit attribuut.
        :param int boom_parameter_nummer: Het ID van de boomparameter van dit attribuut.
        :param int onder_filter_waarde: De ondergrens.
        :param int boven_filter_waarde: De bovengrens.
        """
        Attribuut.__init__(self, attribuut_id, boom_parameter_nummer)

        self._onder_filter_waarde: int = onder_filter_waarde
        """
        De ondergrens om dit attribuut te laten vuren.
        """

        self._boven_filter_waarde: int = boven_filter_waarde
        """
        De bovengrens om dit attribuut te laten vuren.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, subtraject: Subtraject):
        """
        Geeft het aantal malen dat de boomparameter voldoet aan de voorwaarde van dit attribuut.

        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        aantal = self._boom_parameter.tel(None, subtraject)

        if self._onder_filter_waarde <= aantal <= self._boven_filter_waarde:
            return 1

        return 0

# ----------------------------------------------------------------------------------------------------------------------
