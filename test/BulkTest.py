import csv
from unittest import TestCase

from kerapu.Kerapu import Kerapu
from kerapu.lbz.Subtraject import Subtraject


class BulkTest(TestCase):
    """
    Bulk testen.
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
    def __bepaal_zorgproduct(self, subtraject, expected):
        """
        Bepaalt de zorgproductcode van een subtraject.

        :param kerapu.lbz.Subtraject.Subtraject subtraject: Het subtraject.
        """
        zorg_product_groep_code = self.__grouper.bepaal_zorg_product_groep(subtraject)
        subtraject.set_zorg_product_groep_code(zorg_product_groep_code)

        if zorg_product_groep_code != '0':
            zorg_product_code = self.__grouper.bepaal_zorg_product(subtraject, zorg_product_groep_code)
            self.assertEqual(zorg_product_code, expected, subtraject.get_subtraject_nummer())

    # ------------------------------------------------------------------------------------------------------------------
    def bulk_test_file(self, filename):
        """
        Tests against a file with test cases.

        :type: str filename The file with test cases.
        """
        with open(filename, 'rt', encoding='utf-8') as handle:
            csv_reader = csv.reader(handle, lineterminator='\n', delimiter=',')

            subtraject = None
            zorg_product_code = None
            for rij in csv_reader:
                if subtraject and len(rij) > 2:
                    self.__bepaal_zorgproduct(subtraject, zorg_product_code)
                    subtraject = None

                if len(rij) == 2:
                    subtraject.add_zorg_activiteit(rij[0], rij[1])
                else:
                    subtraject = Subtraject(rij[0], rij[1], rij[2], rij[3], rij[4], rij[5], rij[6], rij[7], rij[8])
                    zorg_product_code = rij[9]

            if subtraject:
                self.__bepaal_zorgproduct(subtraject, zorg_product_code)

    # ------------------------------------------------------------------------------------------------------------------
    def test01(self):
        """
        Bulk test.
        """
        self.bulk_test_file('test/var/lib/testset.csv')

# ----------------------------------------------------------------------------------------------------------------------
