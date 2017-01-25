"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class ZorgTypeCode(BoomParameter):
    """
    Klasse voor boomparameter zorgtype.

    Boomparameternummer: 210.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, zorg_type_attribuut_code, subtraject):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat het zorgtype van een subtraject voldoet aan een
        (specialismecode, zorgtypecode) combinatie.

        :param str zorg_type_attribuut_code: De attribuutcode voor (specialismecode, zorgtypecode) combinatie.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_zorg_type_attribuut_telling(zorg_type_attribuut_code)

# ----------------------------------------------------------------------------------------------------------------------
