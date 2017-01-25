"""
Kerapu
"""


class ZorgProductGroep:
    """
    Klasse voor zorgproductgroepen.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, zorg_product_groep_code):
        """
        Object constructor.

        :param str zorg_product_groep_code: De zorgproductgroepcode.
        """
        self._zorg_product_groep_code = zorg_product_groep_code
        """
        De zorgproductgroepcode.

        :type: str
        """

        self._versies = []
        """
        De versies van de zorgproductgroep.

        :type: list[ZorgProductGroepVersie]
        """

    # ------------------------------------------------------------------------------------------------------------------
    def versie_toevoegen(self, versie):
        """
        Voegt een versie toe aan de lijst met versies voor dit zorgproductgroep.

        :param kerapu.Boom.ZorgProductGroepVersie.ZorgProductGroepVersie versie: De toe te voegen versie.
        """
        self._versies.append(versie)

    # ------------------------------------------------------------------------------------------------------------------
    def klim(self, subtraject):
        """
        Bepaalt de zorgproductgroepcode van een subtraject.

        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.
        """
        versie = self.__get_actuele_versie(subtraject)

        return versie.klim(subtraject)

    # ------------------------------------------------------------------------------------------------------------------
    def __get_actuele_versie(self, subtraject):
        """
        Geeft de actuele versie van dit zorgproductgroep voor een subtraject.

        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: kerapu.Boom.ZorgProductGroepVersie.ZorgProductGroepVersie
        """
        for versie in self._versies:
            if versie.is_actueel(subtraject):
                return versie

        raise RuntimeError(
            "Er kan geen actuele versie van zorgproductgroep '%s' gevonden worden voor subtraject '%s" % (
                self._zorg_product_groep_code, subtraject.get_subtraject_nummer()))

# ----------------------------------------------------------------------------------------------------------------------
