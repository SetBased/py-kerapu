"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class SpecialismeCode(BoomParameter):
    """
    Klasse voor boomparameter specialismecode.

    Boomparameternummer: 200.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, specialisme_code, subtraject):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat het uitvoerend specialisme van een subtraject voldoet aan een
        specialismecode.

        :param str specialisme_code: De specialismecode.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_specialisme_telling(specialisme_code)

# ----------------------------------------------------------------------------------------------------------------------
