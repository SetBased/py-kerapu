"""
Kerapu
"""
import csv

from kerapu import clean_code, LEN_SPECIALISME_CODE, LEN_ZORG_VRAAG_CODE, clean_str, clean_date


class ZorgVraag:
    """
    Klasse voor zorgvragen.
    """
    # ------------------------------------------------------------------------------------------------------------------
    __zorg_vraag_tabel = {}
    """
    De zorgvragen referentietabel.

    :type: dict[(str,str),list[dict[str,str]]]
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, specialisme_code, zorg_vraag_code):
        """
        Object constructor.

        :param str specialisme_code: De code van het uitvoerend specialisme.
        :param str zorg_vraag_code: De code van deze zorgvraag.
        """
        self.__specialisme_code = clean_code(specialisme_code, LEN_SPECIALISME_CODE)
        """
        De code van het uitvoerend specialisme.

        :type: str
        """

        self.__zorg_vraag_code = clean_code(zorg_vraag_code, LEN_ZORG_VRAAG_CODE)
        """
        De code van deze zorgvraag.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def init_static(folder):
        """
        Initialiseert alle statistische data.

        :param str folder: De folder met alle goupertabellen.
        """
        ZorgVraag.__lees_zorg_vraag_tabel(folder)

    # ------------------------------------------------------------------------------------------------------------------
    def __get_zorg_vraag_referentie(self, datum):
        """
        Zoekt de referentie data voor deze zorg_vraag in de zorgvraag referentietabel.

        :param datum: De begindatum van het subtraject.

        :rtype: dict[str,str]
        """

        if (self.__specialisme_code, self.__zorg_vraag_code) in self.__zorg_vraag_tabel:
            for referentie in self.__zorg_vraag_tabel[(self.__specialisme_code, self.__zorg_vraag_code)]:
                if referentie['begin_datum'] <= datum <= referentie['eind_datum']:
                    # Een geldige referentie rij gevonden.
                    return referentie

            # Er is geen geldige referentie rij gevonden.
            return None

        else:
            return None

    # ------------------------------------------------------------------------------------------------------------------
    def get_zorg_vraag_attribute_aantal(self, zorg_vraag_attribuut_code, datum):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) data deze diagnose voldoet aan een (specialismecode, zorgvraagcode)
        combinatie op een peildatum.

        :param str zorg_vraag_attribuut_code: De attribuutcode voor (specialismecode, diagnosecode) combinatie.
        :param str datum: De peildatum.

        :rtype: int
        """
        referentie = self.__get_zorg_vraag_referentie(datum)

        if not referentie:
            # De diagnose komt niet voor in de referentie tabel. Geef 0 terug.
            return 0

        if referentie['zorg_vraag_attribute_code'] == zorg_vraag_attribuut_code:
            return 1

        return 0

    # ------------------------------------------------------------------------------------------------------------------
    def get_zorg_vraag_cluster_aantal(self, cluster_code, cluster_nummer, datum):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat deze zorgvraag voorkomt in een zorgvraagcluster op een peildatum.

        :param str cluster_code: De zorgvraagclustercode.
        :param int cluster_nummer: Het clusternummer (0..2).
        :param str datum: De peildatum.

        :rtype: int
        """
        referentie = self.__get_zorg_vraag_referentie(datum)

        if not referentie:
            # Deze zorgvraag komt niet voor in de referentie tabel. Geef 0 terug.
            return 0

        if cluster_nummer == 0:
            return 1

        if 1 <= cluster_nummer <= 2:
            if referentie['zorg_vraag_cluster%d' % cluster_nummer] == cluster_code:
                # Deze zorgvraag komt voor in het gevraagde cluster.
                return 1

            return 0

        raise RuntimeError("Onbekend clusternummer %d." % cluster_nummer)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __lees_zorg_vraag_tabel(folder):
        """
        Leest de zorg_vraag referentietabel (opgeslagen in CSV).

        :param str folder: De folder met alle goupertabellen.
        """
        with open(folder + '/ZorgVragen.csv', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                specialisme_code = clean_code(regel[0], LEN_SPECIALISME_CODE)
                zorg_vraag_code = clean_code(regel[1], LEN_ZORG_VRAAG_CODE)
                zorg_vraag_attribuut_code = clean_str(regel[3])
                zorg_vraag_cluster01 = clean_str(regel[4])
                zorg_vraag_cluster02 = clean_str(regel[5])
                begin_datum = clean_date(regel[6])
                eind_datum = clean_date(regel[7])

                sleutel = (specialisme_code, zorg_vraag_code)

                rij = {'specialisme_code':          specialisme_code,
                       'zorg_vraag_code':           zorg_vraag_code,
                       'zorg_vraag_attribute_code': zorg_vraag_attribuut_code,
                       'zorg_vraag_cluster1':       zorg_vraag_cluster01,
                       'zorg_vraag_cluster2':       zorg_vraag_cluster02,
                       'begin_datum':               begin_datum,
                       'eind_datum':                eind_datum}

                if sleutel not in ZorgVraag.__zorg_vraag_tabel:
                    ZorgVraag.__zorg_vraag_tabel[sleutel] = []

                ZorgVraag.__zorg_vraag_tabel[sleutel].append(rij)

        print("Aantal zorgvragen: %d" % (regel_nummer - 1))

# ----------------------------------------------------------------------------------------------------------------------
