"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class Geslacht(BoomParameter):
    """
    Klasse voor boomparameter geslacht.

    Boomparameternummer: 230.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, geslacht_code, subtraject):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de patient van een subtraject voldoet aan een geslacht.

        :param str geslacht_code: De geslachtscode waartegen getest moet worden.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_geslacht_code_telling(geslacht_code)

# ----------------------------------------------------------------------------------------------------------------------
