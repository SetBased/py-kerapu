"""
Kerapu
"""
import csv

from kerapu import clean_code, clean_date, clean_str, LEN_SPECIALISME_CODE


class Specialisme:
    """
    Klasse voor specialismen.
    """
    # ------------------------------------------------------------------------------------------------------------------
    _specialisme_tabel = {}
    """
    De specialismen referentietabel.
    :type: dict[str,list[dict[str,str]]]
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, specialisme_code):
        """
        Object constructor.

        :param str specialisme_code: De code van het specialisme.
        """
        self.__specialisme_code = clean_code(specialisme_code, LEN_SPECIALISME_CODE)
        """
        De code van het uitvoerend specialisme.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _lees_specialisme_tabel(folder):
        """
        Leest de specialisme referentietabel (opgeslagen in CSV).

        :param str folder: De folder met alle goupertabellen.
        """
        with open(folder + '/Specialismen.csv', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, )
            regel_nummer = 0
            for regel in reader:
                regel_nummer += 1

                # Sla de eerste regel met koppen over.
                if regel_nummer == 1:
                    continue

                specialisme_code = clean_code(regel[0], LEN_SPECIALISME_CODE)
                specialisme_cluster1 = clean_str(regel[4])
                specialisme_cluster2 = clean_str(regel[5])
                begin_datum = clean_date(regel[7])
                eind_datum = clean_date(regel[8])

                rij = {'specialisme_code':     specialisme_code,
                       'specialisme_cluster1': specialisme_cluster1,
                       'specialisme_cluster2': specialisme_cluster2,
                       'begin_datum':          begin_datum,
                       'eind_datum':           eind_datum}

                if specialisme_code not in Specialisme._specialisme_tabel:
                    Specialisme._specialisme_tabel[specialisme_code] = []

                Specialisme._specialisme_tabel[specialisme_code].append(rij)

        print("Aantal specialismen: %d" % (regel_nummer - 1))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def init_static(folder):
        """
        Initialiseert alle statistische data.

        :param str folder: De folder met alle goupertabellen.
        """
        Specialisme._lees_specialisme_tabel(folder)

    # ------------------------------------------------------------------------------------------------------------------
    def __get_specialisme_referentie(self, datum):
        """
        Zoekt de referentie data voor deze specialisme in de specialismen referentietabel.

        :param str datum: De begindatum van het subtraject.

        :rtype: dict[str,str]
        """
        if self.__specialisme_code in self._specialisme_tabel:
            for referentie in self._specialisme_tabel[self.__specialisme_code]:
                if referentie['begin_datum'] <= datum <= referentie['eind_datum']:
                    # Een geldige referentie rij gevonden.
                    return referentie

            # Er is geen geldige referentie rij gevonden.
            return None

        else:
            return None

    # ------------------------------------------------------------------------------------------------------------------
    def get_specialisme_aantal(self, specialisme_code, datum):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat dit specialisme voldoet aan een attributecode op een gegeven datum
        .
        :param str specialisme_code: De attribuutcode waaraan voldaan moet worden.
        :param str datum: De datum.

        :rtype: int
        """
        referentie = self.__get_specialisme_referentie(datum)

        if not referentie:
            # Het specialisme komt niet voor in de referentie tabel. Geef 0 terug.
            return 0

        if referentie['specialisme_code'] == clean_code(specialisme_code, LEN_SPECIALISME_CODE):
            return 1

        return 0

    # ------------------------------------------------------------------------------------------------------------------
    def get_specialisme_cluster_aantal(self, cluster_code, cluster_nummer, datum):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat dit specialisme voldoet aan een clustercode op een gegeven datum.

        :param str cluster_code: De clustercode waaraan voldaan moet worden.
        :param int cluster_nummer: Het clusternummer.
        :param str datum: De datum.

        :rtype: int
        """
        referentie = self.__get_specialisme_referentie(datum)

        if not referentie:
            # Het specialisme komt niet voor in de referentie tabel. Geef 0 terug.
            return 0

        if cluster_nummer == 0:
            return 1

        if 1 <= cluster_nummer <= 2:
            if referentie['specialisme_cluster%d' % cluster_nummer] == cluster_code:
                # Dit specialisme komt voor in het gevraagde cluster.
                return 1

            return 0

        raise RuntimeError("Onbekend clusternummer %d." % cluster_nummer)

# ----------------------------------------------------------------------------------------------------------------------
