"""
Kerapu
"""
from typing import List

from kerapu.boom.ZorgProductGroepVersie import ZorgProductGroepVersie
from kerapu.lbz.Subtraject import Subtraject


class ZorgProductGroep:
    """
    Klasse voor zorgproductgroepen.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, zorg_product_groep_code: str):
        """
        Object constructor.

        :param str zorg_product_groep_code: De zorgproductgroepcode.
        """
        self._zorg_product_groep_code: str = zorg_product_groep_code
        """
        De zorgproductgroepcode.
        """

        self._versies: List[ZorgProductGroepVersie] = []
        """
        De versies van de zorgproductgroep.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def versie_toevoegen(self, versie: ZorgProductGroepVersie):
        """
        Voegt een versie toe aan de lijst met versies voor dit zorgproductgroep.

        :param ZorgProductGroepVersie versie: De toe te voegen versie.
        """
        self._versies.append(versie)

    # ------------------------------------------------------------------------------------------------------------------
    def klim(self, subtraject: Subtraject)-> str:
        """
        Bepaalt de zorgproductgroepcode van een subtraject.

        :param subtraject subtraject: Het subtraject.
        """
        versie = self.__get_actuele_versie(subtraject)

        return versie.klim(subtraject)

    # ------------------------------------------------------------------------------------------------------------------
    def __get_actuele_versie(self, subtraject: Subtraject) -> ZorgProductGroepVersie:
        """
        Geeft de actuele versie van dit zorgproductgroep voor een subtraject.

        :param Subtraject subtraject: Het subtraject.

        :rtype: ZorgProductGroepVersie
        """
        for versie in self._versies:
            if versie.is_actueel(subtraject):
                return versie

        raise RuntimeError(
            "Er kan geen actuele versie van zorgproductgroep '%s' gevonden worden voor subtraject '%s" % (
                self._zorg_product_groep_code, subtraject.subtraject_nummer))

# ----------------------------------------------------------------------------------------------------------------------
