"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class ZorgActiviteitCode(BoomParameter):
    """
    Klasse voor boomparameter zorgactiviteit.

    Boomparameternummers: 300, 400, 500.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, weeg_factor_nummer):
        """
        Object constructor.

        :param int weeg_factor_nummer: Weegfactornummer:

                                       * 0: geen weegfactor
                                       * 1: weegfactor 1
                                       * 2: weegfactor 2
        """
        self._weeg_factor_nummer = weeg_factor_nummer

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, zorg_activiteit_code, subtraject):
        """
        Geeft het aantal zorgactiviteiten (met inachtneming van weegfactor) in een subtraject voldoet aan een
        zorgactiviteitcode.

        :param str zorg_activiteit_code: De zorgactiviteitcode.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_zorg_activiteit_telling(zorg_activiteit_code, self._weeg_factor_nummer)

# ----------------------------------------------------------------------------------------------------------------------
