"""
Kerapu
"""
from kerapu.boom.attribuut.Attribuut import Attribuut


class Attribuut21(Attribuut):
    """
    Klasse voor attributen met toetswijze 2 (tussen) en waarde type 1 (numeriek).
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 attribuut_id,
                 boom_parameter_nummer,
                 onder_filter_waarde,
                 boven_filter_waarde):
        """
        Object constructor.

        :param int attribuut_id: Het ID van dit attribuut.
        :param int boom_parameter_nummer: Het ID van de boomparameter van dit attribuut.
        :param int onder_filter_waarde: De ondergrens.
        :param int boven_filter_waarde: De bovengrens.
        """
        Attribuut.__init__(self, attribuut_id, boom_parameter_nummer)

        self._onder_filter_waarde = onder_filter_waarde
        """
        De ondergrens om dit attribuut te laten vuren.

        :type: int
        """

        self._boven_filter_waarde = boven_filter_waarde
        """
        De bovengrens om dit attribuut te laten vuren.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, subtraject):
        """
        Geeft het aantal malen dat de boomparameter voldoet aan de voorwaarde van dit attribuut.

        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        aantal = self._boom_parameter.tel(None, subtraject)

        if self._onder_filter_waarde <= aantal <= self._boven_filter_waarde:
            return 1

        return 0

# ----------------------------------------------------------------------------------------------------------------------
