"""
Kerapu
"""
from typing import List

from kerapu.boom.attribuut_groep_koppeling import AttribuutGroepKoppeling
from kerapu.lbz.Subtraject import Subtraject


class AttribuutGroep:
    """
    Klasse voor attribuutgroep.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 attribute_groep_id: int,
                 aantal_voorwaarden_voor_true: int,
                 koppelingen: List[AttribuutGroepKoppeling]):
        """
        Object constructor.

        :param int attribute_groep_id: Het ID van deze attribuutgroep.
        :param int aantal_voorwaarden_voor_true: Het minimale aantal voorwaarden waaraan moet worden voldaan.
        :param list[kerapu.boom.attribuut_groep_koppeling.AttribuutGroepKoppeling.AttribuutGroepKoppeling] koppelingen:
               De attribuutgroepkoppelingen.
        """
        self._attribute_groep_id: int = attribute_groep_id
        """
        Het ID van deze attribuutgroep.
        """

        self._aantal_voorwaarden_voor_true: int = aantal_voorwaarden_voor_true
        """
        Het minimale aantal voorwaarden waaraan moet worden voldaan om deze attribuutgroep te laten vuren.
        """

        self._koppelingen: List[AttribuutGroepKoppeling] = koppelingen
        """
        De attribuutgroepkoppelingen.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def test(self, subtraject: Subtraject) -> bool:
        """
        Test of een subtraject voldoet aan de voorwaarden van deze attribuutgroep.

        :param Subtraject subtraject: Het subtraject.

        :rtype: bool
        """
        aantal = 0
        for koppeling in self._koppelingen:
            if koppeling.test(subtraject):
                aantal += 1

        return aantal >= self._aantal_voorwaarden_voor_true

# ----------------------------------------------------------------------------------------------------------------------
