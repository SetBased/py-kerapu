"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class ZorgVraagCode(BoomParameter):
    """
    Klasse voor boomparameter zorgvraagcode.

    Boomparameternummers: 220.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, zorg_vraag_attribuut_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de zorgvraag van een subtraject voldoet aan een
        (specialismecode, zorgvraagcode).

        :param str zorg_vraag_attribuut_code: De attribuutcode voor (specialismecode, zorgvraagcode).
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_zorg_vraag_attribuut_telling(zorg_vraag_attribuut_code)

# ----------------------------------------------------------------------------------------------------------------------
