"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class Geslacht(BoomParameter):
    """
    Klasse voor boomparameter geslacht.

    Boomparameternummer: 230.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, geslacht_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de patient van een subtraject voldoet aan een geslacht.

        :param str geslacht_code: De geslachtscode waartegen getest moet worden.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.telling_geslacht_code(geslacht_code)

# ----------------------------------------------------------------------------------------------------------------------
