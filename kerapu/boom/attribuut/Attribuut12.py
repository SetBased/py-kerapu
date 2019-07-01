"""
Kerapu
"""
from kerapu.boom.attribuut.Attribuut import Attribuut
from kerapu.lbz.Subtraject import Subtraject


class Attribuut12(Attribuut):
    """
    Klasse voor attributen met toetswijze 1 (gelijk) en waarde type 2 (alfanumeriek).
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, attribuut_id: int, boom_parameter_nummer: int, filter_waarde: str):
        """
        Object constructor.

        :param int attribuut_id: Het ID van dit attribuut.
        :param int boom_parameter_nummer: Het ID van de boomparameter van dit attribuut.
        :param str filter_waarde: De filter waarde.
        """
        Attribuut.__init__(self, attribuut_id, boom_parameter_nummer)

        self._filter_waarde = filter_waarde
        """
        De waarde om dit attribuut the laten vuren.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen dat de boomparameter voldoet aan de voorwaarde van dit attribuut.

        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return self._boom_parameter.tel(self._filter_waarde, subtraject)

# ----------------------------------------------------------------------------------------------------------------------
