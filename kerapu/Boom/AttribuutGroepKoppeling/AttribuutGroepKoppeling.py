"""
Kerapu

:copyright: 2015-2016 Set Based IT Consultancy
:licence: MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import abc

from kerapu.Boom.Attribuut.Attribuut import Attribuut


# ----------------------------------------------------------------------------------------------------------------------
class AttribuutGroepKoppeling:
    """
    Abstract klasse voor attribuutgroepkoppelingen.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, attribute_groep_id, attribuut):
        """
        Object constructor.

        :param int attribute_groep_id: Het ID van deze koppeling.
        :param Attribuut attribuut: Het attribuut van deze koppeling.
        """
        self._attribute_groep_id = attribute_groep_id
        """
        Het ID van deze attribuutgroepkoppeling.

        :type: int
        """

        self._attribuut = attribuut
        """
        Het attribuut van deze koppeling.

        :type: Attribuut
        """

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def test(self, subtraject):
        """
        Test of een subtraject voldoet aan een attribuutgroepkoppeling.

        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: bool
        """""
        pass

# ----------------------------------------------------------------------------------------------------------------------
