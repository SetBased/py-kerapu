"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class SpecialismeCode(BoomParameter):
    """
    Klasse voor boomparameter specialismecode.

    Boomparameternummer: 200.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, specialisme_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat het uitvoerend specialisme van een subtraject voldoet aan een
        specialismecode.

        :param str specialisme_code: De specialismecode.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.telling_specialisme(specialisme_code)

# ----------------------------------------------------------------------------------------------------------------------
