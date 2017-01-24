"""
Kerapu
"""


class ZorgProductGroepVersie:
    """
    Klasse voor versies zorgproductgroepversies.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 zorg_product_groep_code,
                 beslis_regel,
                 begin_datum,
                 eind_datum):
        """
        Object constructor.

        :param str zorg_product_groep_code: De zorgproductgroepcode.
        :param kerapu.Boom.BeslisRegel.BeslisRegel beslis_regel: De beslisregel behoorden bij de zorgproductgroepcode.
        :param str begin_datum: Begindatum van het interval waarvoor deze versie van toepassing is.
        :param str eind_datum: Einddatum van het interval waarvoor deze versie van toepassing is.
        """
        self._zorg_product_groep_code = zorg_product_groep_code
        """
        De zorgproductgroepcode.

        :type: str
        """

        self._beslis_regel = beslis_regel
        """
        De beslisregel behoorden bij de zorgproductgroepcode.

        :type: kerapu.Boom.BeslisRegel.BeslisRegel
        """

        self._begin_datum = begin_datum
        """
        Begindatum van het interval waarvoor deze versie van toepassing is.

        :type: str
        """

        self._eind_datum = eind_datum
        """
        Einddatum van het interval waarvoor deze versie van toepassing is.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    def is_actueel(self, subtraject):
        """
        Geeft True als deze versie actueel is voor een subtraject, anders False.

        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: bool
        """
        return self._begin_datum <= subtraject.get_begin_datum() <= self._eind_datum

    # ------------------------------------------------------------------------------------------------------------------
    def klim(self, subtraject):
        """
        Klimt door de beslisboom een geeft het uiteindelijk gevonden label terug.

        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: str
        """
        return self._beslis_regel.klim(subtraject)

# ----------------------------------------------------------------------------------------------------------------------
