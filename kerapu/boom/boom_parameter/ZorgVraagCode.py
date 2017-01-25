"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class ZorgVraagCode(BoomParameter):
    """
    Klasse voor boomparameter zorgvraagcode.

    Boomparameternummers: 220.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, zorg_vraag_attribuut_code, subtraject):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de zorgvraag van een subtraject voldoet aan een
        (specialismecode, zorgvraagcode).

        :param str zorg_vraag_attribuut_code: De attribuutcode voor (specialismecode, zorgvraagcode).
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_zorg_vraag_attribuut_telling(zorg_vraag_attribuut_code)

# ----------------------------------------------------------------------------------------------------------------------
