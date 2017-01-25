"""
Kerapu
"""
from kerapu.boom.attribuut.Attribuut import Attribuut


class Attribuut12(Attribuut):
    """
    Klasse voor attributen met toetswijze 1 (gelijk) en waarde type 2 (alfanumeriek).
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, attribuut_id, boom_parameter_nummer, filter_waarde):
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
    def tel(self, subtraject):
        """
        Geeft het aantal malen dat de boomparameter voldoet aan de voorwaarde van dit attribuut.

        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return self._boom_parameter.tel(self._filter_waarde, subtraject)

# ----------------------------------------------------------------------------------------------------------------------
