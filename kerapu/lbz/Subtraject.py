from typing import Optional, List

from kerapu import clean_code, LEN_ZORG_ACTIVITEIT_CODE, LEN_ZORG_PRODUCT_GROEP_CODE, LEN_ZORG_PRODUCT_CODE
from kerapu.lbz.Diagnose import Diagnose
from kerapu.lbz.Patient import Patient
from kerapu.lbz.Specialisme import Specialisme
from kerapu.lbz.ZorgActiviteit import ZorgActiviteit
from kerapu.lbz.ZorgInstelling import ZorgInstelling
from kerapu.lbz.ZorgType import ZorgType
from kerapu.lbz.ZorgVraag import ZorgVraag


class Subtraject:
    """
    Klasse voor subtrajecten.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 subtraject_nummer: str,
                 specialisme_code: str,
                 diagnose_code: str,
                 zorg_type_code: str,
                 zorg_vraag_code: str,
                 begin_datum: str,
                 geboorte_datum: str,
                 geslacht_code: str,
                 zorg_instelling_code: str) -> None:
        """
        Object constructor.

        :param str subtraject_nummer: Het substrajectnummer.
        :param str specialisme_code: Het (uitvoerend)specialismecode.
        :param str diagnose_code:  De Diagnosecode.
        :param str zorg_type_code: Het zorgtypecode.
        :param str zorg_vraag_code: De zorgvraagcode.
        :param str begin_datum:  De begindatum van het subtraject.
        :param str geboorte_datum: De geboortedatum van de patient.
        :param str geslacht_code: De code voor het geslacht van de patient.
        :param str zorg_instelling_code: De AGB-code van de uitvoerende zorginstelling.
        """
        self.__subtraject_nummer: str = subtraject_nummer
        """
        Het subtrajectnummer.
        """

        self.__specialisme: Specialisme = Specialisme(specialisme_code)
        """
        Het uitvoerend specialisme.
        """

        self.__begin_datum: str = begin_datum
        """
        De begindatum van het subtraject.
        """

        self.__patient: Patient = Patient(geboorte_datum, geslacht_code)
        """
        De patient.
        """

        self.__zorg_instelling: ZorgInstelling = ZorgInstelling(zorg_instelling_code)
        """
        De zorginstelling.
        """

        self.__zorg_type: ZorgType = ZorgType(specialisme_code, zorg_type_code)
        """
        Het zorgtype.
        """

        self.__zorg_vraag: ZorgVraag = ZorgVraag(specialisme_code, zorg_vraag_code)
        """
        De zorgvraag.
        """

        self.__diagnose: Diagnose = Diagnose(specialisme_code, diagnose_code)
        """
        De diagnose.
        """

        self.__zorg_activiteiten: List[ZorgActiviteit] = []
        """
        De zorgactiviteiten.
        """

        self.__zorg_product_code: Optional[str] = None
        """
        De zorgproductcode (zoals afgeleid door Kerapu).
        """

        self.__zorg_product_groep_code: Optional[str] = None
        """
        De zorgproductgroepcode (zoals afgeleid door Kerapu).
        """

    # ------------------------------------------------------------------------------------------------------------------
    def add_zorg_activiteit(self, zorg_activiteit_code: str, aantal: int) -> None:
        """
        Voegt een zorgactiviteit toe and dit subtraject.

        :param str zorg_activiteit_code: De zorgactiviteitcode.
        :param int aantal: Het aantal malen (of eenheden) dat de zorgactiviteit is uitgevoerd.
        """
        self.__zorg_activiteiten.append(ZorgActiviteit(zorg_activiteit_code, aantal))

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def begin_datum(self) -> str:
        """
        Geeft de begindatum van dit subtraject.

        :rtype: str
        """
        return self.__begin_datum

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def leeftijd(self) -> int:
        """
        Geeft de leeftijd van de patient van dit subtraject.

        :rtype: int
        """
        return self.__patient.leeftijd(self.__begin_datum)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def subtraject_nummer(self) -> str:
        """
        Geeft het subtrajectnummer van dit subtraject.

        :rtype: str
        """
        return self.__subtraject_nummer

    # ------------------------------------------------------------------------------------------------------------------
    def telling_behandel_klasse(self, behandel_klasse_code: str, weeg_factor_nummer: int) -> int:
        """
        Geeft het aantal zorgactiviteiten (met inachtneming van weegfactor) dat in dit subtraject voorkomt in een
        behandelklasse.

        :param str behandel_klasse_code: De behandelklassecode waartegen getest moet worden.
        :param int weeg_factor_nummer: Het weegfactornummer (0..2).

        :rtype: int
        """
        aantal = 0
        for zorg_activiteit in self.__zorg_activiteiten:
            aantal += zorg_activiteit.behandel_klasse_aantal(self.__zorg_product_groep_code,
                                                             behandel_klasse_code,
                                                             weeg_factor_nummer,
                                                             self.__begin_datum)

        return aantal

    # ------------------------------------------------------------------------------------------------------------------
    def telling_diagnose_attribuut(self, diagnose_attribuut_code: str) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de diagnose van dit subtraject voldoet aan een
        (specialismecode, diagnosecode) combinatie.

        :param str diagnose_attribuut_code: De attribuutcode voor de (specialismecode, diagnosecode) combinatie.

        :rtype: int
        """
        return self.__diagnose.diagnose_attribute_aantal(diagnose_attribuut_code, self.__begin_datum)

    # ------------------------------------------------------------------------------------------------------------------
    def telling_diagnose_cluster(self, cluster_code: str, cluster_nummer: int) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat in dit subtraject voldoet aan een diagnoseclustercode.

        :param str cluster_code: De cluster_code waartegen getest moet worden.
        :param int cluster_nummer: Het clusternummer (1..6).

        :rtype: int
        """
        return self.__diagnose.diagnose_cluster_aantal(cluster_code, cluster_nummer, self.__begin_datum)

    # ------------------------------------------------------------------------------------------------------------------
    def telling_geslacht_code(self, geslacht_code: str) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de patient van dit subtraject voldoet aan een geslacht.

        :param str geslacht_code: De geslachtscode waartegen getest moet worden.

        :rtype: int
        """
        if self.__patient.geslacht_code == geslacht_code:
            return 1

        return 0

    # ------------------------------------------------------------------------------------------------------------------
    def telling_specialisme(self, specialisme_code: str) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat het uitvoerend specialisme van dit subtraject voldoet aan een
        specialismecode.

        :param str specialisme_code: De specialismecode.

        :rtype: int
        """
        return self.__specialisme.specialisme_aantal(specialisme_code, self.__begin_datum)

    # ------------------------------------------------------------------------------------------------------------------
    def telling_specialisme_cluster(self, cluster_code: str, cluster_nummer: int) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat het uitvoerend specialisme van dit subtraject voldoet aan een
        specialismecluster.

        :param str cluster_code: De clustercode waartegen getest moet worden.
        :param int cluster_nummer: Het clusternummer (1..2).

        :rtype: int
        """
        return self.__specialisme.specialisme_cluster_aantal(cluster_code, cluster_nummer, self.__begin_datum)

    # ------------------------------------------------------------------------------------------------------------------
    def telling_zorg_activiteit(self, zorg_activiteit_code: str, weeg_factor_nummer: int) -> int:
        """
        Geeft het aantal zorgactiviteiten (met inachtneming van weegfactor) dat in dit subtraject voldoet aan een
        zorgactiviteitcode.

        :param str zorg_activiteit_code: De zorgactiviteitcode.
        :param int weeg_factor_nummer: Het weegfactornummer (0..2).

        :rtype: int
        """
        aantal = 0
        zorg_activiteit_code = clean_code(zorg_activiteit_code, LEN_ZORG_ACTIVITEIT_CODE)
        for zorg_activiteit in self.__zorg_activiteiten:
            aantal += zorg_activiteit.zorg_activiteit_aantal(zorg_activiteit_code,
                                                             weeg_factor_nummer,
                                                             self.__begin_datum)

        return aantal

    # ------------------------------------------------------------------------------------------------------------------
    def telling_zorg_activiteit_cluster(self,
                                        cluster_code: str,
                                        cluster_nummer: int,
                                        weeg_factor_nummer: int) -> int:
        """
        Geeft het aantal zorgactiviteiten (met inachtneming van weegfactor) dat in dit subtraject voorkomt in een
        zorgactiviteitcluster.

        :param str cluster_code: De zorgactiviteitclustercode.
        :param int cluster_nummer: Het clusternummer (1..10).
        :param int weeg_factor_nummer: Het weegfactornummer (0..2).

        :rtype: int
        """
        aantal = 0
        for zorg_activiteit in self.__zorg_activiteiten:
            aantal += zorg_activiteit.zorg_activiteit_cluster_aantal(cluster_code,
                                                                     cluster_nummer,
                                                                     weeg_factor_nummer,
                                                                     self.__begin_datum)

        return aantal

    # ------------------------------------------------------------------------------------------------------------------
    def telling_zorg_instelling(self, agb_code: str) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de zorginstelling van dit subtraject voldoet aan AGB-code.

        :param str agb_code: De AGB-code waaraan de zorginstelling moet voldoen.

        :rtype: int
        """
        return self.__zorg_instelling.zorg_instelling_aantal(agb_code)

    # ------------------------------------------------------------------------------------------------------------------
    def telling_zorg_type_attribuut(self, zorg_type_attribuut_code: str) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de zorgtype van dit subtraject voldoet aan een
        (specialismecode, zorgtypecode) combinatie.

        :param str zorg_type_attribuut_code: De attribuutcode voor de (specialismecode, zorgtypecode) combinatie.

        :rtype: int
        """
        return self.__zorg_type.zorg_type_attribute_aantal(zorg_type_attribuut_code, self.__begin_datum)

    # ------------------------------------------------------------------------------------------------------------------
    def telling_zorg_vraag_attribuut(self, zorg_vraag_attribuut_code: str) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de zorgvraag van dit subtraject voldoet aan een
        (specialismecode, zorgvraagcode) combinatie.

        :param str zorg_vraag_attribuut_code: De attribuutcode voor de (specialismecode, zorgvraagcode) combinatie.

        :rtype: int
        """
        return self.__zorg_vraag.zorg_vraag_attribute_aantal(zorg_vraag_attribuut_code, self.__begin_datum)

    # ------------------------------------------------------------------------------------------------------------------
    def telling_zorg_vraag_cluster(self, cluster_code: str, cluster_nummer: int) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de zorgvraag van een subtraject voorkomt in een zorgvraagcluster.

        :param str cluster_code: De cluster_code waartegen getest moet worden.
        :param int cluster_nummer: Het clusternummer (1..2).

        :rtype: int
        """
        return self.__zorg_vraag.zorg_vraag_cluster_aantal(cluster_code, cluster_nummer, self.__begin_datum)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def zorg_product_code(self) -> Optional[str]:
        """
        Geeft de zorgproductcode van dit subtraject.

        :rtype: str|None
        """
        return self.__zorg_product_code

    # ------------------------------------------------------------------------------------------------------------------
    @zorg_product_code.setter
    def zorg_product_code(self, zorg_product_code: Optional[str]) -> None:
        """
        Zet de zorgproductcode van dit subtraject.

        :param str zorg_product_code: De zorgproductcode.
        """
        if zorg_product_code != '' and zorg_product_code is not None:
            self.__zorg_product_code = clean_code(zorg_product_code, LEN_ZORG_PRODUCT_CODE)
        else:
            self.__zorg_product_groep_code = None

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def zorg_product_groep_code(self) -> Optional[str]:
        """
        Geeft de zorgproductgroepcode van dit subtraject.

        :rtype: str|None
        """
        return self.__zorg_product_groep_code

    # ------------------------------------------------------------------------------------------------------------------
    @zorg_product_groep_code.setter
    def zorg_product_groep_code(self, zorg_product_groep_code: Optional[str]) -> None:
        """
        Zet de zorgproductgroepcode van dit subtraject.

        :param str zorg_product_groep_code: De zorgproductgroepcode.
        """
        if zorg_product_groep_code != '' and zorg_product_groep_code is not None:
            self.__zorg_product_groep_code = clean_code(zorg_product_groep_code, LEN_ZORG_PRODUCT_GROEP_CODE)
        else:
            self.__zorg_product_groep_code = None

# ----------------------------------------------------------------------------------------------------------------------
