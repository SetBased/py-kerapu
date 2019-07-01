"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class ZorgInstellingCode(BoomParameter):
    """
    Klasse voor boomparameter zorginstelling.

    Boomparameternummer: 110.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, zorg_instelling_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat het zorginstelling van een subtraject voldoet een zorginstellingcode.

        :param str zorg_instelling_code: De AGB-code waaraan de zorginstelling moet voldoen.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.telling_zorg_instelling(zorg_instelling_code)

# ----------------------------------------------------------------------------------------------------------------------
