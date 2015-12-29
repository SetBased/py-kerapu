"""
Kerapu

:copyright: 2015-2016 Set Based IT Consultancy
:licence: MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import csv

from kerapu import *
from kerapu.Boom.Attribuut import maak_attribuut
from kerapu.Boom.AttribuutGroep import AttribuutGroep
from kerapu.Boom.AttribuutGroepKoppeling import maak_attribuut_groep_koppeling
from kerapu.Boom.BeslisRegel import BeslisRegel
from kerapu.Lbz.Diagnose import Diagnose
from kerapu.Boom.ZorgProductGroep import ZorgProductGroep
from kerapu.Boom.ZorgProductGroepVersie import ZorgProductGroepVersie
from kerapu.Lbz.Specialisme import Specialisme
from kerapu.Lbz.ZorgActiviteit import ZorgActiviteit
from kerapu.Lbz.ZorgType import ZorgType
from kerapu.Lbz.ZorgVraag import ZorgVraag

# ----------------------------------------------------------------------------------------------------------------------


class Kerapu:
    """
    Een implementatie van de grouper in Python.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self._zorgproductgroep_boom = {}
        """
        De zorgproductgroepboom. Sleutel is zorgproductgroepcode.
        :type: dict[str, ZorgProductGroep]
        """

        self._beslisregels = {}
        """
        Alle beslisregels. Sleutel is het ID van de beslisregel.
        :type: dict[int, BeslisRegel]
        """

        self._attribuutgroepen = {}
        """
        Alle attribuutgroepen. Sleutel is het ID van de attribuutgroep.
        :type: dict[int, AttribuutGroep]
        """

        self._attribuut_groep_koppelingen = {}
        """
        Alle attribuutgroepkoppelingen. Sleutel is het ID van de attribuutgroep.
        :type: dict[int, list[AttribuutGroepKoppeling]]
        """

        self._attributen = {}
        """
        Alle attributen. Sleutel is het ID van het attribuut.
        :type: dict[int, Attribuut]
        """

    # ------------------------------------------------------------------------------------------------------------------
    def init_static(self, folder):
        """
        Initialiseert alle statistische data.

        :param str folder: De folder met alle goupertabellen.
        """
        self._lees_attribuut_tabel(folder)
        self._lees_attribuut_groep_koppeling_tabel(folder)
        self._lees_attribuut_groepen_tabel(folder)
        self._lees_beslis_regel_tabel(folder)
        self._lees_zorg_product_groepen(folder)

        Diagnose.init_static(folder)
        Specialisme.init_static(folder)
        ZorgActiviteit.init_static(folder)
        ZorgType.init_static(folder)
        ZorgVraag.init_static(folder)

    # ------------------------------------------------------------------------------------------------------------------
    def _lees_attribuut_tabel(self, folder):
        """
        Leest de attribuuttabel (opgeslagen in CSV).
        
        :type str folder: De folder met alle groupertabellen in CSV-formaat.
        """
        with open(folder + '/Attributen.csv') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                attribuut_id = int(regel[0])
                boom_parameter_nummer = int(regel[2])
                filter_toets_wijze = int(regel[3])
                filter_waarde_type = int(regel[4])
                onder_filter_waarde = clean_str(regel[5])
                boven_filter_waarde = clean_str(regel[6])

                self._attributen[attribuut_id] = maak_attribuut(attribuut_id,
                                                                boom_parameter_nummer,
                                                                filter_toets_wijze,
                                                                filter_waarde_type,
                                                                onder_filter_waarde,
                                                                boven_filter_waarde)

        print("Aantal attributen: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    def _lees_attribuut_groep_koppeling_tabel(self, folder):
        """
        Leest de  attribuutgroepkoppelingen (opgeslagen in CSV).
        
        :type str folder: De folder met alle groupertabellen in CSV-formaat.
        """
        with open(folder + '/AttribuutGroepKoppelingen.csv') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                attribuut_groep_id = int(regel[1])
                attribuut_id = int(regel[2])
                attribuut_toets_wijze = int(regel[3])
                onder_toets_waarde = clean_int(regel[4])
                boven_toets_waarde = clean_int(regel[5])

                if attribuut_groep_id not in self._attribuut_groep_koppelingen:
                    self._attribuut_groep_koppelingen[attribuut_groep_id] = []

                if attribuut_id not in self._attributen:
                    raise RuntimeError("Onbekend attribuut: '%d'" % attribuut_id)

                koppeling = maak_attribuut_groep_koppeling(attribuut_groep_id,
                                                           self._attributen[attribuut_id],
                                                           attribuut_toets_wijze,
                                                           onder_toets_waarde,
                                                           boven_toets_waarde)

                self._attribuut_groep_koppelingen[attribuut_groep_id].append(koppeling)

        print("Aantal attribuutgroepkoppelingen: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    def _lees_attribuut_groepen_tabel(self, folder):
        """
        Leest de attribuutgroepen (opgeslagen in CSV).
        
        :type str folder: De folder met alle groupertabellen in CSV-formaat.
        """
        with open(folder + '/AttribuutGroepen.csv') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                attribuut_groep_id = int(regel[0])
                aantal_voorwaarden_voor_true = int(regel[2])

                if attribuut_groep_id not in self._attribuut_groep_koppelingen:
                    raise RuntimeError("Onbekende koppeling: '%d'" % attribuut_groep_id)

                self._attribuutgroepen[attribuut_groep_id] = AttribuutGroep(attribuut_groep_id,
                                                                            aantal_voorwaarden_voor_true,
                                                                            self._attribuut_groep_koppelingen[
                                                                                attribuut_groep_id])

        print("Aantal attributen: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    def _lees_beslis_regel_tabel(self, folder):
        """
        Leest de beslisregels (opgeslagen in CSV).
        
        :type str folder: De folder met alle groupertabellen in CSV-formaat.
        """
        verrijkingen = {}
        with open(folder + '/BeslisRegels.csv') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                beslis_regel_id = int(regel[0])
                attribuut_groep_id = int(regel[1])
                beslist_regel_id_true = clean_int(regel[2])
                beslist_regel_id_false = clean_int(regel[3])
                label_true = clean_str(regel[4])
                label_false = clean_str(regel[5])
                indicatie_aanspraakbeperking = clean_bool(regel[6])

                if attribuut_groep_id not in self._attribuutgroepen:
                    raise RuntimeError("Onbekende attribuutgroep: '%d'" % attribuut_groep_id)

                verrijkingen[beslis_regel_id] = (beslist_regel_id_true, beslist_regel_id_false)

                self._beslisregels[beslis_regel_id] = BeslisRegel(beslis_regel_id,
                                                                  self._attribuutgroepen[attribuut_groep_id],
                                                                  label_true,
                                                                  label_false,
                                                                  indicatie_aanspraakbeperking)

        # Verrijk alle beslisregels met beslisregels voor true en false.
        for beslis_regel_id, (beslist_regel_id_true, beslist_regel_id_false) in verrijkingen.items():
            beslist_regel_true = self._beslisregels.get(beslist_regel_id_true, None)
            beslist_regel_false = self._beslisregels.get(beslist_regel_id_false, None)
            self._beslisregels[beslis_regel_id].verrijk(beslist_regel_true, beslist_regel_false)

        print("Aantal beslisregels: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    def _lees_zorg_product_groepen(self, folder):
        """
        Leest de zorgproductgroepen (opgeslagen in CSV).
        
        :type str folder: De folder met alle groupertabellen in CSV-formaat.
        """
        with open(folder + '/ZorgProductGroepen.csv') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                zorg_product_groep_code = clean_str(regel[0])
                beslist_regel_id_start = int(regel[2])
                begin_datum = clean_date(regel[3])
                eind_datum = clean_date(regel[4])

                if zorg_product_groep_code not in self._zorgproductgroep_boom:
                    self._zorgproductgroep_boom[zorg_product_groep_code] = ZorgProductGroep(zorg_product_groep_code)

                versie = ZorgProductGroepVersie(zorg_product_groep_code,
                                                self._beslisregels[beslist_regel_id_start],
                                                begin_datum,
                                                eind_datum)
                self._zorgproductgroep_boom[zorg_product_groep_code].versie_toevoegen(versie)

        print("Aantal zorgproductgroep versies: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    def bepaal_zorg_product_groep(self, subtraject):
        """
        Bepaalt de zorgproductgroep van een subtraject.

        :param Subject subtraject: Het subtraject waarvoor de zorgproductgroep moet worden bepaalt.

        :rtype: str
        """
        top_boom = self._zorgproductgroep_boom['0']

        return top_boom.klim(subtraject)

    # ------------------------------------------------------------------------------------------------------------------
    def bepaal_zorg_product(self, subtraject, zorg_product_groep_code):
        """
        Bepaalt de zorgproduct van een subtraject.

        :param Subject subtraject: Het subtraject waarvoor de zorgproductcode moet worden bepaalt.
        :param str zorg_product_groep_code: De zorgproductgroep van het subtraject.

        :rtype: str
        """
        top_boom = self._zorgproductgroep_boom[zorg_product_groep_code]

        return top_boom.klim(subtraject)

# ----------------------------------------------------------------------------------------------------------------------
