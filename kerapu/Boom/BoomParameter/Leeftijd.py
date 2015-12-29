"""
Kerapu

:copyright: 2015-2016 Set Based IT Consultancy
:licence: MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from kerapu.Boom.BoomParameter.BoomParameter import BoomParameter


# ----------------------------------------------------------------------------------------------------------------------
class Leeftijd(BoomParameter):
    """
    Klasse voor boomparameter leeftijd.

    Boomparameternummer: 100.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, leeg, subtraject):
        """
        Geeft de leeftijd van de patient van een subtraject.

        :param None leeg: Wordt niet gebruikt.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_leeftijd()


# ----------------------------------------------------------------------------------------------------------------------
