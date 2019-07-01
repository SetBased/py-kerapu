from unittest import TestCase

from kerapu.Kerapu import Kerapu
from kerapu.lbz.Subtraject import Subtraject


class VoorbeeldTest(TestCase):
    """
    Test cases als in voorbeelden.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, method_name='runTest'):
        """
        Object constructor.
        """
        TestCase.__init__(self, method_name)

        self.__grouper = Kerapu()
        self.__grouper.init_static('test/var/lib')

    # ------------------------------------------------------------------------------------------------------------------
    def test00(self):
        """
        Test voorbeeld 0, geen verrichtingen, door niemand.
        """
        # Maak een subtraject object.
        subtraject = Subtraject('1',
                                '0000',
                                '0000',
                                '00',
                                '000',
                                '2012-01-01',
                                '2000-01-01',
                                'M',
                                '01234567')

        # Bepaal zorgproductgroep en zorgproduct.
        zorg_product_code = self.__grouper.bepaal_zorg_product(subtraject)
        self.assertEqual(zorg_product_code, '019999018')
        self.assertEqual(subtraject.zorg_product_groep_code, '019999')
        self.assertEqual(subtraject.zorg_product_code, '019999018')

    # ------------------------------------------------------------------------------------------------------------------
    def test01(self):
        """
        Test voorbeeld 1.
        """
        # Maak een subtraject object.
        subtraject = Subtraject('1',
                                '0303',
                                '0280',
                                '11',
                                '000',
                                '2012-01-01',
                                '2000-01-01',
                                'M',
                                '01234567')

        # Voeg uitgevoerde zorgactiviteiten aan het subtraject toe.
        subtraject.add_zorg_activiteit('038940', 1)
        subtraject.add_zorg_activiteit('038941', 1)
        subtraject.add_zorg_activiteit('190012', 1)
        subtraject.add_zorg_activiteit('190015', 1)

        # Bepaal zorgproductgroep en zorgproduct.
        zorg_product_code = self.__grouper.bepaal_zorg_product(subtraject)
        self.assertEqual(zorg_product_code, '199299012')
        self.assertEqual(subtraject.zorg_product_groep_code, '199299')
        self.assertEqual(subtraject.zorg_product_code, '199299012')

    # ------------------------------------------------------------------------------------------------------------------
    def test02(self):
        """
        Test voorbeeld 2.
        """
        # Maak een subtraject object.
        subtraject = Subtraject('1',
                                '0305',
                                '1805',
                                '11',
                                '000',
                                '2019-02-01',
                                '1971-09-01',
                                'M',
                                '01234567')

        # Voeg uitgevoerde zorgactiviteiten aan het subtraject toe.
        subtraject.add_zorg_activiteit('039460', 1)
        subtraject.add_zorg_activiteit('190013', 1)

        # Bepaal zorgproductgroep en zorgproduct.
        zorg_product_code = self.__grouper.bepaal_zorg_product(subtraject)
        self.assertEqual(zorg_product_code, '131999165')
        self.assertEqual(subtraject.zorg_product_groep_code, '131999')
        self.assertEqual(subtraject.zorg_product_code, '131999165')

    # ------------------------------------------------------------------------------------------------------------------
    def test03(self):
        """
        Test voorbeeld 3.
        """
        # Maak een subtraject object.
        subtraject = Subtraject('1',
                                '0305',
                                '2055',
                                '11',
                                '000',
                                '2019-03-01',
                                '1960-02-01',
                                'M',
                                '01234567')

        # Voeg uitgevoerde zorgactiviteiten aan het subtraject toe.
        subtraject.add_zorg_activiteit('089602', 1)
        subtraject.add_zorg_activiteit('190013', 1)
        subtraject.add_zorg_activiteit('190060', 1)

        # Bepaal zorgproductgroep en zorgproduct.
        zorg_product_code = self.__grouper.bepaal_zorg_product(subtraject)
        self.assertEqual(zorg_product_code, '131999228')
        self.assertEqual(subtraject.zorg_product_groep_code, '131999')
        self.assertEqual(subtraject.zorg_product_code, '131999228')

    # ------------------------------------------------------------------------------------------------------------------
    def test04(self):
        """
        Test voorbeeld 4.
        """
        # Maak een subtraject object.
        subtraject = Subtraject('1',
                                '0305',
                                '3409',
                                '11',
                                '000',
                                '2019-03-01',
                                '1948-12-01',
                                'M',
                                '01234567')

        # Voeg uitgevoerde zorgactiviteiten aan het subtraject toe.
        subtraject.add_zorg_activiteit('089090', 1)
        subtraject.add_zorg_activiteit('089602', 1)
        subtraject.add_zorg_activiteit('190013', 1)
        subtraject.add_zorg_activiteit('190060', 1)

        # Bepaal zorgproductgroep en zorgproduct.
        zorg_product_code = self.__grouper.bepaal_zorg_product(subtraject)
        self.assertEqual(zorg_product_code, '199299119')
        self.assertEqual(subtraject.zorg_product_groep_code, '199299')
        self.assertEqual(subtraject.zorg_product_code, '199299119')

    # ------------------------------------------------------------------------------------------------------------------
    def test05(self):
        """
        Test voorbeeld 5.
        """
        # Maak een subtraject object.
        subtraject = Subtraject('1',
                                '0308',
                                '2501',
                                '11',
                                '000',
                                '2019-05-01',
                                '1961-11-01',
                                'M',
                                '01234567')

        # Voeg uitgevoerde zorgactiviteiten aan het subtraject toe.
        subtraject.add_zorg_activiteit('190060', 1)

        # Bepaal zorgproductgroep en zorgproduct.
        zorg_product_code = self.__grouper.bepaal_zorg_product(subtraject)
        self.assertEqual(zorg_product_code, '131999277')
        self.assertEqual(subtraject.zorg_product_groep_code, '131999')
        self.assertEqual(subtraject.zorg_product_code, '131999277')

# ------------------------------------------------------------------------------------------------------------------
