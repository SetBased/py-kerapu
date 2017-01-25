from unittest import TestCase

from kerapu.Kerapu import Kerapu
from kerapu.lbz.Subtraject import Subtraject


class VoorbeeldTest(TestCase):
    """
    Test cases als in voorbeelden.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Test voorbeeld 1.
        """
        # Maak en initialiseer Grouper object.
        grouper = Kerapu()
        grouper.init_static('test/var/lib')

        # Maak Grouper object en laad boom- en referentietabellen.
        subtraject = Subtraject('1',  # Subtrajectnummer
                                '0303',  # Zorgverlenerspecificatiecode
                                '0280',  # Diagnosecode
                                '11',  # Zorgtypecode
                                '000',  # Zorgvraagcode
                                '2012-01-01',  # Begindatum subtraject
                                '2000-01-01',  # Geboortedatum
                                'M')  # Geslachtscode

        # Maak Grouper object en laad Boom- en referentie tabellen.
        subtraject.add_zorg_activiteit('038940', 1)
        subtraject.add_zorg_activiteit('038941', 1)
        subtraject.add_zorg_activiteit('190012', 1)
        subtraject.add_zorg_activiteit('190015', 1)

        # Bepaal zorgproductgroep en zorgproduct.
        zorg_product_groep_code = grouper.bepaal_zorg_product_groep(subtraject)
        zorg_product_code = grouper.bepaal_zorg_product(subtraject, zorg_product_groep_code)
        self.assertEqual(zorg_product_code, '199299012')

# ------------------------------------------------------------------------------------------------------------------
