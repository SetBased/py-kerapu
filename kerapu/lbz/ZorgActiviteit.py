"""
Kerapu
"""
import csv

from kerapu import clean_code, LEN_ZORG_ACTIVITEIT_CODE, clean_int, clean_str, clean_date, LEN_ZORG_PRODUCT_GROEP_CODE


class ZorgActiviteit:
    """
    Klasse voor zorgactiviteiten.
    """
    # ------------------------------------------------------------------------------------------------------------------
    __zorg_activiteiten_tabel = {}
    """
    De zorgactiviteiten referentietabel.

    :type: dict[str,list[dict[str,str]]]
    """

    __zorg_activiteiten_vertaal_tabel = {}
    """
    De zorgactiviteiten vertaaltabel.

    :type: dict[str,list[dict[str,str]]]
    """

    __behandel_klassen_tabel = {}
    """
    De behandelklassen referentietabel.

    :type: dict[(str,str,str),list[dict[str,str]]]
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, zorg_activiteit_code, aantal):
        """
        Object constructor.

        :param str zorg_activiteit_code: De code van deze zorgactiviteit.
        :param int aantal: Het aantal malen dat deze zorgactiviteit is uitgevoerd.
        """
        self.__zorg_activiteit_code = clean_code(zorg_activiteit_code, LEN_ZORG_ACTIVITEIT_CODE)
        """
        De code van deze zorgactiviteit.

        :type: str
        """

        self.__aantal = clean_int(aantal, 0)
        """
        Het aantal malen dat deze zorgactiviteit is uitgevoerd.

        :type: int
        """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __lees_zorgactiviteiten_tabel(folder):
        """
        Leest de zorgactiviteiten referentietabel (opgeslagen in CSV).
        """
        with open(folder + '/ZorgActiviteiten.csv', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                zorg_activiteit_code = clean_code(regel[0], LEN_ZORG_ACTIVITEIT_CODE)
                zorg_activiteit_cluster01 = clean_str(regel[2])
                zorg_activiteit_cluster02 = clean_str(regel[3])
                zorg_activiteit_cluster03 = clean_str(regel[4])
                zorg_activiteit_cluster04 = clean_str(regel[5])
                zorg_activiteit_cluster05 = clean_str(regel[6])
                zorg_activiteit_cluster06 = clean_str(regel[7])
                zorg_activiteit_cluster07 = clean_str(regel[8])
                zorg_activiteit_cluster08 = clean_str(regel[9])
                zorg_activiteit_cluster09 = clean_str(regel[10])
                zorg_activiteit_cluster10 = clean_str(regel[11])
                zorg_activiteit_weeg_factor1 = clean_int(regel[12])
                zorg_activiteit_weeg_factor2 = clean_int(regel[13])
                begin_datum = clean_date(regel[20])
                eind_datum = clean_date(regel[21])

                sleutel = zorg_activiteit_code

                rij = {'zorg_activiteit_code':         zorg_activiteit_code,
                       'zorg_activiteit_cluster01':    zorg_activiteit_cluster01,
                       'zorg_activiteit_cluster02':    zorg_activiteit_cluster02,
                       'zorg_activiteit_cluster03':    zorg_activiteit_cluster03,
                       'zorg_activiteit_cluster04':    zorg_activiteit_cluster04,
                       'zorg_activiteit_cluster05':    zorg_activiteit_cluster05,
                       'zorg_activiteit_cluster06':    zorg_activiteit_cluster06,
                       'zorg_activiteit_cluster07':    zorg_activiteit_cluster07,
                       'zorg_activiteit_cluster08':    zorg_activiteit_cluster08,
                       'zorg_activiteit_cluster09':    zorg_activiteit_cluster09,
                       'zorg_activiteit_cluster10':    zorg_activiteit_cluster10,
                       'zorg_activiteit_weeg_factor1': zorg_activiteit_weeg_factor1,
                       'zorg_activiteit_weeg_factor2': zorg_activiteit_weeg_factor2,
                       'begin_datum':                  begin_datum,
                       'eind_datum':                   eind_datum}

                if sleutel not in ZorgActiviteit.__zorg_activiteiten_tabel:
                    ZorgActiviteit.__zorg_activiteiten_tabel[sleutel] = []

                ZorgActiviteit.__zorg_activiteiten_tabel[sleutel].append(rij)

        print("Aantal zorgactiviteiten: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __lees_zorg_activiteiten_vertaal_tabel(folder):
        """
        Leest de zorgactiviteiten vertaaltabel (opgeslagen in CSV).
        """
        with open(folder + '/VertaalZorgActiviteiten.csv', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                zorg_activiteit_code = clean_code(regel[0], LEN_ZORG_ACTIVITEIT_CODE)
                zorg_activiteit_code_oud = clean_code(regel[2], LEN_ZORG_ACTIVITEIT_CODE)
                begin_datum = clean_date(regel[4])
                eind_datum = clean_date(regel[5])

                sleutel = zorg_activiteit_code

                rij = {'zorg_activiteit_code':     zorg_activiteit_code,
                       'zorg_activiteit_code_oud': zorg_activiteit_code_oud,
                       'begin_datum':              begin_datum,
                       'eind_datum':               eind_datum}

                if sleutel not in ZorgActiviteit.__zorg_activiteiten_vertaal_tabel:
                    ZorgActiviteit.__zorg_activiteiten_vertaal_tabel[sleutel] = []

                ZorgActiviteit.__zorg_activiteiten_vertaal_tabel[sleutel].append(rij)

        print("Aantal zorgactiviteit vertalingen: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __lees_behandel_klasse_tabel(folder):
        """
        Leest de behandelklasse tabel (opgeslagen in CSV).
        """
        with open(folder + '/BehandelKlassen.csv', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                zorg_product_groep_code = clean_code(regel[0], LEN_ZORG_PRODUCT_GROEP_CODE)
                zorg_activiteit_code = clean_code(regel[1], LEN_ZORG_ACTIVITEIT_CODE)
                behandel_klasse_code = clean_str(regel[2])
                begin_datum = clean_date(regel[4])
                eind_datum = clean_date(regel[5])

                sleutel = (zorg_product_groep_code, zorg_activiteit_code, behandel_klasse_code)

                rij = {'zorg_product_groep_code': zorg_product_groep_code,
                       'zorg_activiteit_code':    zorg_activiteit_code,
                       'behandel_klasse_code':    behandel_klasse_code,
                       'begin_datum':             begin_datum,
                       'eind_datum':              eind_datum}

                if sleutel not in ZorgActiviteit.__behandel_klassen_tabel:
                    ZorgActiviteit.__behandel_klassen_tabel[sleutel] = []

                ZorgActiviteit.__behandel_klassen_tabel[sleutel].append(rij)

        print("Aantal behandelklassen: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def init_static(folder):
        """
        Initialiseert alle statistische data.

        :param str folder: De folder met alle goupertabellen.
        """
        ZorgActiviteit.__lees_behandel_klasse_tabel(folder)
        ZorgActiviteit.__lees_zorgactiviteiten_tabel(folder)
        ZorgActiviteit.__lees_zorg_activiteiten_vertaal_tabel(folder)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __vertaal_zorgactiviteit_code(zorg_activiteit_code, datum):
        """
        Vertaalt een "nieuwe" zorgactiviteitcode naar een "oude" zorgactiviteitcode die geldig is ten tijde van het
        begin van het subtraject.

        :param str zorg_activiteit_code: De "nieuwe" zorgactiviteitcode.
        :param str datum: De begindatum van het subtraject.
        """
        zorg_activiteit_code = clean_code(zorg_activiteit_code, LEN_ZORG_ACTIVITEIT_CODE)

        if zorg_activiteit_code in ZorgActiviteit.__zorg_activiteiten_vertaal_tabel:
            for vertaling in ZorgActiviteit.__zorg_activiteiten_vertaal_tabel[zorg_activiteit_code]:
                if vertaling['begin_datum'] <= datum <= vertaling['eind_datum']:
                    # Een geldige vertaling gevonden. geef de "oude" zorgactiviteitcode terug.
                    return vertaling['zorg_activiteit_code_oud']

            # Er is geen vertaling van toepassing ten tijde van het begin van het subtraject. Geef de gegeven
            # zorgactiviteitcode terug.
            return zorg_activiteit_code
        else:
            # Er is geen enkele vertaling voor de zorgactiviteitcode. Geef de gegeven zorgactiviteitcode terug.
            return zorg_activiteit_code

    # ------------------------------------------------------------------------------------------------------------------
    def __get_zorg_activiteit_referentie(self, datum):
        """
        Zoekt de referentie data voor deze zorgactiviteit in de zorgactiviteiten referentietabel.

        :param datum: De begindatum van het subtraject.

        :rtype: dict[str,str]
        """
        # Vertaal de zorgactiviteitcode naar een "oude" zorgactiviteitcode.
        zorg_activiteit_code = ZorgActiviteit.__vertaal_zorgactiviteit_code(self.__zorg_activiteit_code, datum)

        if zorg_activiteit_code in self.__zorg_activiteiten_tabel:
            for referentie in self.__zorg_activiteiten_tabel[zorg_activiteit_code]:
                if referentie['begin_datum'] <= datum <= referentie['eind_datum']:
                    # Een geldige referentie rij gevonden.
                    return referentie

            # Er is geen geldige referentie rij gevonden.
            return None

        else:
            return None

    # ------------------------------------------------------------------------------------------------------------------
    def __get_behandel_klasse_referentie(self, zorg_product_groep_code, behandel_klasse_code, datum):
        """
        Zoekt de referentie data voor deze zorgactiviteit in de behandelklasse referentietabel.

        :param str zorg_product_groep_code: De zorgproductgroepcode van het subtraject.
        :param str behandel_klasse_code: De gevraagde behandelklassecode
        :param str datum: De begindatum van het subtraject.

        :rtype: dict[str,str]
        """
        # Vertaal de zorgactiviteitcode naar een "oude" zorgactiviteitcode.
        zorg_activiteit_code = ZorgActiviteit.__vertaal_zorgactiviteit_code(self.__zorg_activiteit_code, datum)

        sleutel = (zorg_product_groep_code, zorg_activiteit_code, behandel_klasse_code)
        if sleutel in self.__behandel_klassen_tabel:
            for referentie in self.__behandel_klassen_tabel[sleutel]:
                if referentie['begin_datum'] <= datum <= referentie['eind_datum']:
                    # Een geldige referentie rij gevonden.
                    return referentie

        # Er is geen geldige referentie rij gevonden.
        return None

    # ------------------------------------------------------------------------------------------------------------------
    def get_behandel_klasse_aantal(self, zorg_product_groep_code, behandel_klasse_code, weeg_factor_nummer, datum):
        """
        Geeft het aantal malen (met inachtneming van weegfactor) dat deze zorgactiviteit voorkomt in een
        behandleklasse op een peildatum.

        :param str zorg_product_groep_code: De zorgproductgroepcode van het subtraject van deze zorgactiviteit.
        :param str behandel_klasse_code: De behandelklasse.
        :param int weeg_factor_nummer: Het weegfactornummer (0..2).
        :param str datum: De peildatum.

        :rtype: int
        """
        referentie = self.__get_behandel_klasse_referentie(zorg_product_groep_code, behandel_klasse_code, datum)

        if not referentie:
            # De (zorgproductgroepcode,zorgactiviteitcode,behandelklassecode) komt niet voor in de referentie tabel.
            # Geef 0 terug.
            return 0

        if weeg_factor_nummer == 0:
            # Weegfactor is niet van toepassing.
            return self.__aantal

        if weeg_factor_nummer == 1:
            return referentie['zorg_activiteit_weeg_factor1'] * self.__aantal

        if weeg_factor_nummer == 2:
            return referentie['zorg_activiteit_weeg_factor2'] * self.__aantal

        raise RuntimeError("Onbekend weegfactornummer %d." % weeg_factor_nummer)

    # ------------------------------------------------------------------------------------------------------------------
    def get_zorg_activiteit_aantal(self, zorg_activiteit_code, weeg_factor_nummer, datum):
        """
        Geeft het aantal malen (met inachtneming van weegfactor) dat deze zorgactiviteit voldoet aan een
        zorgactiviteitcode.

        :param str zorg_activiteit_code: De zorgactiviteitcode.
        :param int weeg_factor_nummer: Het weegfactornummer (0..2).
        :param str datum: De peildatum.

        :rtype: int
        """
        referentie = self.__get_zorg_activiteit_referentie(datum)

        if not referentie:
            # De zorgactiviteitcode komt niet voor in de referentie tabel. Geef 0 terug.
            return 0

        if self.__zorg_activiteit_code != clean_code(zorg_activiteit_code, LEN_ZORG_ACTIVITEIT_CODE):
            return 0

        if weeg_factor_nummer == 0:
            # Weegfactor is niet van toepassing.
            return self.__aantal

        if weeg_factor_nummer == 1:
            return referentie['zorg_activiteit_weeg_factor1'] * self.__aantal

        if weeg_factor_nummer == 2:
            return referentie['zorg_activiteit_weeg_factor2'] * self.__aantal

        raise RuntimeError("Onbekend weegfactornummer %d." % weeg_factor_nummer)

    # ------------------------------------------------------------------------------------------------------------------
    def get_zorg_activiteit_cluster_aantal(self, cluster_code, cluster_nummer, weeg_factor_nummer, datum):
        """
        Geeft het aantal malen (met inachtneming van weegfactor) dat deze zorgactiviteit voorkomt in een
        zorgactiviteitcluster.

        :param str cluster_code: De zorgactiviteitclustercode.
        :param int cluster_nummer: het cluster nummber (1..10).
        :param int weeg_factor_nummer: Het weegfactornummer (0..2).
        :param str datum: De peildatum.

        :rtype: int
        """
        referentie = self.__get_zorg_activiteit_referentie(datum)

        if not referentie:
            # De zorgactiviteitcode komt niet voor in de referentie tabel. Geef 0 terug.
            return 0

        if 1 <= cluster_nummer <= 10:
            if referentie['zorg_activiteit_cluster%02d' % cluster_nummer] != cluster_code:
                # Deze zorgactiviteit kom niet voor in het gevraagde cluster.
                return 0

            if weeg_factor_nummer == 0:
                # Weegfactor is niet van toepassing.
                return self.__aantal

            if weeg_factor_nummer == 1:
                return referentie['zorg_activiteit_weeg_factor1'] * self.__aantal

            if weeg_factor_nummer == 2:
                return referentie['zorg_activiteit_weeg_factor2'] * self.__aantal

            raise RuntimeError("Onbekend weegfactornummer %d." % weeg_factor_nummer)

        raise RuntimeError("Onbekend clusternummer %d." % cluster_nummer)

# ----------------------------------------------------------------------------------------------------------------------
