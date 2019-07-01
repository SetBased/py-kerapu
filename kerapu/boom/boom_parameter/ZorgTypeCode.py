"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class ZorgTypeCode(BoomParameter):
    """
    Klasse voor boomparameter zorgtype.

    Boomparameternummer: 210.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, zorg_type_attribuut_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat het zorgtype van een subtraject voldoet aan een
        (specialismecode, zorgtypecode) combinatie.

        :param str zorg_type_attribuut_code: De attribuutcode voor (specialismecode, zorgtypecode) combinatie.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.telling_zorg_type_attribuut(zorg_type_attribuut_code)

# ----------------------------------------------------------------------------------------------------------------------
