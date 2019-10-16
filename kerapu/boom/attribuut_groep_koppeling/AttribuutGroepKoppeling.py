import abc

from kerapu.boom.attribuut.Attribuut import Attribuut
from kerapu.lbz.Subtraject import Subtraject


class AttribuutGroepKoppeling:
    """
    Abstract klasse voor attribuutgroepkoppelingen.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, attribute_groep_id: int, attribuut: Attribuut):
        """
        Object constructor.

        :param int attribute_groep_id: Het ID van deze koppeling.
        :param Attribuut attribuut: Het attribuut van deze koppeling.
        """
        self._attribute_groep_id: int = attribute_groep_id
        """
        Het ID van deze attribuutgroepkoppeling.
        """

        self._attribuut: Attribuut = attribuut
        """
        Het attribuut van deze koppeling.
        """

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def test(self, subtraject: Subtraject) -> bool:
        """
        Test of een subtraject voldoet aan een attribuutgroepkoppeling.

        :param Subtraject subtraject: Het subtraject.

        :rtype: bool
        """""
        pass

# ----------------------------------------------------------------------------------------------------------------------
