"""
Kerapu
"""
from kerapu.boom.attribuut.Attribuut import Attribuut
from kerapu.boom.attribuut_groep_koppeling.AttribuutGroepKoppeling import AttribuutGroepKoppeling
from kerapu.lbz.Subtraject import Subtraject


class AttribuutGroepKoppeling2(AttribuutGroepKoppeling):
    """
    Klasse voor attribuutgroepkoppelingen met filtertoetswijze 2 (tussen onder- en bovengrens).
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 attribute_groep_id: int,
                 attribuut: Attribuut,
                 onder_toets_waarde: int,
                 boven_toets_waarde: int):
        """
        Object constructor.

        :param int attribute_groep_id: Het ID van deze koppeling.
        :param Attribuut attribuut: Het attribuut van deze koppeling.
        :param int onder_toets_waarde: De ondergrens.
        :param int boven_toets_waarde: De bovengrens.
        """
        AttribuutGroepKoppeling.__init__(self, attribute_groep_id, attribuut)

        self._onder_toets_waarde = onder_toets_waarde
        """
        De ondergrens om deze koppeling the laten vuren.

        :type: int
        """

        self._boven_toets_waarde = boven_toets_waarde
        """
        De bovengrens om deze koppeling the laten vuren.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    def test(self, subtraject: Subtraject) -> bool:
        """
        Test of een subtraject voldoet aan een attribuutgroepkoppeling.

        :param Subtraject subtraject: Het subtraject.

        :rtype: bool
        """
        aantal = self._attribuut.tel(subtraject)

        return self._onder_toets_waarde <= aantal <= self._boven_toets_waarde

# ----------------------------------------------------------------------------------------------------------------------
